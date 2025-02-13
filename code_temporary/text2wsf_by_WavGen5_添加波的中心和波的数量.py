import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import yaml
import argparse
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
import cv2
import json

def load_config(config_path):
    """加载配置文件"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def save_video(frames, save_path, fps=20):
    """保存视频"""
    h, w = frames[0].shape[:2]
    writer = cv2.VideoWriter(
        save_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps, (w, h)
    )
    
    for frame in frames:
        writer.write(frame)
    writer.release()

def get_timesteps(config):
    """获取需要渲染的时间步"""
    if config['generation']['mode'] == 'image':
        return [config['generation']['time']['timestep']]
    else:
        start = config['generation']['time']['start']
        end = config['generation']['time']['end']
        fps = config['generation']['time']['fps']
        n_frames = int((end - start) * fps)
        return np.linspace(start, end, n_frames)

class CameraParams:
    def __init__(self, position, rotation=(0,0,0), fov=60):
        self.position = np.array(position)  # (x, y, z)
        self.rotation = np.array(rotation)  # (pitch, yaw, roll)
        self.fov = fov
        self.compute_matrices()
    
    def compute_matrices(self):
        self.view_matrix = self.compute_view_matrix()
        self.projection_matrix = self.compute_projection_matrix()
    
    def compute_view_matrix(self):
        # 从欧拉角计算旋转矩阵
        pitch, yaw, roll = self.rotation
        Rx = np.array([[1, 0, 0],
                      [0, np.cos(pitch), -np.sin(pitch)],
                      [0, np.sin(pitch), np.cos(pitch)]])
        
        Ry = np.array([[np.cos(yaw), 0, np.sin(yaw)],
                      [0, 1, 0],
                      [-np.sin(yaw), 0, np.cos(yaw)]])
        
        Rz = np.array([[np.cos(roll), -np.sin(roll), 0],
                      [np.sin(roll), np.cos(roll), 0],
                      [0, 0, 1]])
        
        R = Rz @ Ry @ Rx
        t = self.position
        
        view_matrix = np.eye(4)
        view_matrix[:3, :3] = R
        view_matrix[:3, 3] = t
        
        return view_matrix
    
    def compute_projection_matrix(self):
        aspect_ratio = 1.0
        near = 0.1
        far = 100.0
        
        f = 1.0 / np.tan(np.radians(self.fov) / 2)
        proj_matrix = np.zeros((4, 4))
        
        proj_matrix[0, 0] = f / aspect_ratio
        proj_matrix[1, 1] = f
        proj_matrix[2, 2] = (far + near) / (near - far)
        proj_matrix[2, 3] = 2 * far * near / (near - far)
        proj_matrix[3, 2] = -1
        
        return proj_matrix

class MultiScaleWaveFunction:
    def __init__(self, config):
        self.config = config
        self.scales = config["wave_field"].get("scales", [1.0])
        self.scale_weights = config["wave_field"].get("scale_weights", [1.0])
    
    def schrodinger_wave(self, x, y, z, params, scale, t=0):
        """带中心控制和方向性衰减的3D波函数"""
        # 增加中心位置参数
        k_x, k_y, k_z, omega, sigma_x, sigma_y, sigma_z, decay_x, decay_y, decay_z, center_x, center_y, center_z = params
        
        # 计算相对中心的坐标
        dx = x - center_x
        dy = y - center_y
        dz = z - center_z
        
        # 平面波相位 (相对中心)
        phase = (k_x*dx + k_y*dy + k_z*dz)*scale - omega*t
        
        # 高斯形状控制 (相对中心)
        shape = torch.exp(-((dx/(sigma_x + 1e-6))**2 + 
                          (dy/(sigma_y + 1e-6))**2 + 
                          (dz/(sigma_z + 1e-6))**2)/2)
        
        # 方向性衰减 (相对中心)
        decay = torch.exp(-(decay_x*dx.abs() + decay_y*dy.abs() + decay_z*dz.abs()))
        
        # 组合所有效果
        psi = shape * decay * torch.exp(1j * phase)
        return psi
    
    def superposition(self, coords, params, t=0):
        """时间依赖的多尺度量子态叠加"""
        x, y, z = coords[..., 0], coords[..., 1], coords[..., 2]
        waves = []
        
        for scale, weight in zip(self.scales, self.scale_weights):
            scale_waves = []
            for wave_params in params:
                wave = self.schrodinger_wave(x, y, z, wave_params, scale, t)
                scale_waves.append(wave)
            waves.append(weight * sum(scale_waves))
        
        return sum(waves)
    
    def probability_density(self, psi):
        return torch.abs(psi)**2
    
    def evaluate_3d(self, coords, params, t=0):
        """评估指定时刻的3D空间中的波函数"""
        psi = self.superposition(coords, params, t)
        return psi

class WaveFunctionFeatures(nn.Module):
    """波函数特征提取器"""
    def __init__(self, input_dim=4, hidden_dim=64, output_dim=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
    
    def forward(self, wave_features):
        """
        输入: [batch, ..., 4] (实部、虚部、振幅、相位)
        输出: [batch, ..., output_dim]
        """
        return self.net(wave_features)
    
class WSF:
    """World Snapshot Field with Time Evolution"""
    def __init__(self, config):
        self.config = config
        self.quantum_wave = MultiScaleWaveFunction(config)
        self.feature_extractor = WaveFunctionFeatures()
        
        # 场存储
        self.views = {}  # 存储多个视角的量子态
        self.camera_params = {}
        self.unified_field = None
        self.current_time = 0.0  # 当前时间
        
        # 初始化神经网络
        self.pixel_net = nn.Sequential(
            nn.Conv3d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv3d(64, 4, 1)  # RGB + 概率
        )
    
    def add_view(self, view_id, quantum_state, camera_params):
        self.views[view_id] = quantum_state
        self.camera_params[view_id] = camera_params
    
    def set_time(self, t):
        """设置当前时间"""
        self.current_time = t
    
    def compute_view_weight(self, point, camera_params):
        to_camera = camera_params.position - point
        distance = np.linalg.norm(to_camera)
        
        camera_forward = self.get_camera_forward(camera_params)
        direction_weight = np.dot(to_camera / distance, camera_forward)
        
        return direction_weight / (distance + 1e-6)
    
    def get_camera_forward(self, camera_params):
        rotation_matrix = camera_params.view_matrix[:3, :3]
        return rotation_matrix @ np.array([0, 0, -1])
    
    def merge_views(self, t=None):
        """在指定时刻合并视角"""
        if t is not None:
            self.set_time(t)
            
        if not self.views:
            return
            
        # 1. 初始化3D网格
        grid_coords = self.generate_grid_coords()
        
        # 2. 对每个点计算量子态叠加
        psi_field = torch.zeros(grid_coords.shape[:-1], dtype=torch.complex64)
        feature_field = torch.zeros(*grid_coords.shape[:-1], 32)
        
        for point_idx in np.ndindex(*grid_coords.shape[:-1]):
            point = grid_coords[point_idx]
            # 计算叠加态
            psi = self.compute_quantum_superposition(point)
            psi_field[point_idx] = psi
            
            # 提取特征
            wave_features = torch.stack([
                psi.real, psi.imag,
                torch.abs(psi), torch.angle(psi)
            ])
            feature_field[point_idx] = self.feature_extractor(wave_features)
        
        # 3. 生成RGB和概率
        outputs = self.pixel_net(feature_field.permute(3, 0, 1, 2).unsqueeze(0))
        rgb = torch.sigmoid(outputs[:, :3])
        prob = torch.sigmoid(outputs[:, 3:])
        
        # 4. 应用概率阈值
        mask = prob > self.config["grid"].get("prob_threshold", 0.5)
        self.unified_field = {
            'psi': psi_field,
            'features': feature_field,
            'rgb': rgb * mask,
            'prob': prob,
            'time': self.current_time
        }
    
    def compute_quantum_superposition(self, point):
        psi_total = 0
        weights = 0
        
        for view_id, quantum_state in self.views.items():
            camera = self.camera_params[view_id]
            weight = self.compute_view_weight(point, camera)
            
            # 加入时间参数
            psi = self.quantum_wave.evaluate_3d(
                point,
                quantum_state.wave_params,
                self.current_time
            )
            
            psi_total += weight * psi
            weights += weight
        
        if weights > 0:
            psi_total /= torch.sqrt(weights)
            
        return psi_total
    
    def generate_grid_coords(self):
        x = torch.linspace(-1, 1, self.config["grid"]["size"])
        y = torch.linspace(-1, 1, self.config["grid"]["size"])
        z = torch.linspace(-1, 1, self.config["grid"]["size"])
        grid_x, grid_y, grid_z = torch.meshgrid(x, y, z)
        return torch.stack([grid_x, grid_y, grid_z], dim=-1)
    
    def render_view(self, camera_params, t=None):
        """在指定时刻渲染视角"""
        if t is not None:
            self.merge_views(t)
            
        if self.unified_field is None:
            return None
            
        # 渲染流程...
        rays = self.generate_view_rays(camera_params)
        sampled_points = self.sample_along_rays(rays)
        features = self.interpolate_features(sampled_points)
        rgb = self.render_features(features)
        
        return rgb

    def generate_video(self, camera_params, start_time=0.0, end_time=12.0, fps=20):
        """生成视频序列"""
        frames = []
        times = np.linspace(start_time, end_time, int((end_time - start_time) * fps))
        
        for t in tqdm(times):
            frame = self.render_view(camera_params, t)
            frames.append(frame)
            
        return frames

class QuantumStateEncoder(nn.Module):
    def __init__(self, text_dim=768, hidden_dim=256, num_waves=512):  # 改为512组
        super().__init__()
        self.num_waves = num_waves
        self.text_encoder = nn.Sequential(
            nn.Linear(text_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # 为num_waves个波生成参数
        self.wave_param_net = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_waves * 13)  # 每个波13个参数
        )
    
    def forward(self, text_embedding, t=0):
        features = self.text_encoder(text_embedding)
        wave_params = self.wave_param_net(features)
        # 重塑为num_waves组参数: [batch_size, num_waves, 13]
        return wave_params.view(-1, self.num_waves, 13)

class Text2WSF:
    def __init__(self, config):
        self.config = config
        self.quantum_encoder = QuantumStateEncoder()
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.text_encoder = AutoModel.from_pretrained("bert-base-uncased")
        
    def encode_text(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        outputs = self.text_encoder(**inputs)
        return outputs.last_hidden_state.mean(dim=1)
    
    def generate_quantum_state(self, text_embedding, t=0):
        """生成带时间信息的量子态参数"""
        wave_params = self.quantum_encoder(text_embedding, t)
        return {
            'wave_params': wave_params,
            't': t
        }
    
    def get_camera_params(self, view_name=None, position=None):
        """获取相机参数"""
        if position is not None:
            return CameraParams(position)
            
        if view_name is None:
            view_name = self.config['camera']['default_view']
            
        position = self.config['camera']['views'][view_name]
        return CameraParams(position)
    
    def generate_views(self, text, camera_positions=None, t=0):
        """生成多个视角的量子态"""
        text_embedding = self.encode_text(text)
        base_state = self.generate_quantum_state(text_embedding, t)
        
        views = {}
        camera_params = {}
        
        # 使用配置文件中的相机位置
        if camera_positions is None:
            camera_positions = list(self.config['camera']['views'].values())
            
        for view_id, pos in enumerate(camera_positions):
            camera = CameraParams(pos)
            view_state = self.transform_quantum_state(base_state, camera)
            views[view_id] = view_state
            camera_params[view_id] = camera
            
        return views, camera_params
    
    def generate_wsf(self, text, mode='image', t=None, camera=None):
        """生成WSF，支持图像和视频模式
        Args:
            text (str): 输入文本描述
            mode (str): 'image' 或 'video'
            t (float): 指定时刻（仅用于image模式）
            camera (str/tuple): 相机视角名称或位置
        """
        # 1. 创建WSF对象
        wsf = WSF(self.config)
        
        # 2. 设置时间
        if mode == 'image':
            t = t if t is not None else self.config['generation']['time']['timestep']
        else:
            t = self.config['generation']['time']['start']
            
        # 3. 获取相机参数
        if isinstance(camera, str):
            camera = self.get_camera_params(camera)
        elif isinstance(camera, (list, tuple)):
            camera = self.get_camera_params(position=camera)
        else:
            camera = self.get_camera_params()
            
        # 4. 生成和添加视角
        views, camera_params = self.generate_views(text, t=t)
        for view_id in views:
            wsf.add_view(view_id, views[view_id], camera_params[view_id])
            
        # 5. 根据模式处理
        if mode == 'image':
            wsf.merge_views(t)
            return wsf.render_view(camera)
        else:
            start_t = self.config['generation']['time']['start']
            end_t = self.config['generation']['time']['end']
            fps = self.config['generation']['time']['fps']
            return wsf.generate_video(camera, start_t, end_t, fps)
        
class WSDataset(torch.utils.data.Dataset):
    def __init__(self, text_file, data_dir, data_type='wsv'):
        """
        Args:
            text_file: 包含每行文本描述的文件
            data_dir: 包含.wsv/.wsg文件的目录
            data_type: 'wsv'或'wsg'
        """
        self.data_dir = data_dir
        self.data_type = data_type
        
        # 读取文本描述
        with open(text_file, 'r') as f:
            self.text_descriptions = f.readlines()
            self.text_descriptions = [x.strip() for x in self.text_descriptions]
            
    def __len__(self):
        return len(self.text_descriptions)
        
    def __getitem__(self, idx):
        text = self.text_descriptions[idx]
        file_id = f"{idx:08d}"
        
        if self.data_type == 'wsv':
            data_path = os.path.join(self.data_dir, f"{file_id}.wsv")
            target_field = self.load_wsv(data_path)
        else:
            data_path = os.path.join(self.data_dir, f"{file_id}.wsg") 
            target_field = self.load_wsg(data_path)
            
        return {
            'text': text,
            'target_field': target_field
        }
        
    def load_wsv(self, path):
        """加载视频场景"""
        with open(path, 'rb') as f:
            field_data = np.load(f)
        return torch.from_numpy(field_data)
        
    def load_wsg(self, path):
        """加载图像场景"""
        with open(path, 'rb') as f:
            field_data = np.load(f)
        return torch.from_numpy(field_data)

class WSTrainer:
    def __init__(self, config):
        self.config = config
        self.model = Text2WSF(config)
        
        # 初始化数据集
        if config['training']['mode'] == 'mixed':
            self.train_datasets = [
                WSDataset(config['data']['text_file'], 
                         config['data']['wsv_dir'], 'wsv'),
                WSDataset(config['data']['text_file'],
                         config['data']['wsg_dir'], 'wsg')
            ]
            self.train_loaders = [
                DataLoader(dataset, 
                          batch_size=config['training']['batch_size'],
                          shuffle=True)
                for dataset in self.train_datasets
            ]
        else:
            self.train_dataset = WSDataset(
                config['data']['text_file'],
                config['data'][f"{config['training']['mode']}_dir"],
                config['training']['mode']
            )
            self.train_loader = DataLoader(
                self.train_dataset,
                batch_size=config['training']['batch_size'],
                shuffle=True
            )
            
        # GRPO训练设置
        self.G = config['training']['group_size']
        
    def compute_accuracy_reward(self, generated_field, target_field):
        """计算生成结果的准确性奖励"""
        # 提取特征
        gen_features = self.model.feature_extractor(generated_field)
        target_features = self.model.feature_extractor(target_field)
        
        # 计算相似度
        similarity = F.cosine_similarity(
            gen_features.flatten(2),
            target_features.flatten(2),
            dim=2
        )
        
        return similarity
        
    def training_step(self, batch):
        text, target_field = batch['text'], batch['target_field']
        
        # 采样一组生成结果
        wave_params_group = []
        field_group = []
        for _ in range(self.G):
            views, camera_params = self.model.generate_views(
                text, self.config['camera']['views'].values()
            )
            
            wsf = WSF(self.config)
            for view_id in views:
                wsf.add_view(view_id, views[view_id], camera_params[view_id])
            wsf.merge_views()
            
            wave_params_group.append(views)
            field_group.append(wsf.unified_field)
        
        # 计算rewards
        rewards = []
        for field in field_group:
            reward = self.compute_accuracy_reward(field, target_field)
            rewards.append(reward)
            
        # 计算advantages
        advantages = self.compute_advantage(rewards)
        
        # GRPO更新
        self.update_policy(wave_params_group, advantages)
        
    def compute_advantage(self, rewards):
        rewards = torch.tensor(rewards)
        advantages = (rewards - rewards.mean()) / (rewards.std() + 1e-8)
        return advantages
        
    def update_policy(self, wave_params_group, advantages):
        """使用GRPO更新策略"""
        # 计算policy ratio
        old_probs = self.compute_probs(wave_params_group)
        new_probs = self.compute_probs(wave_params_group)
        ratio = new_probs / old_probs
        
        # 计算GRPO loss
        loss = -(ratio * advantages).mean()
        
        # 更新模型
        loss.backward()
        # 更新优化器
        
    def train(self):
        """训练循环"""
        for epoch in range(self.config['training']['epochs']):
            if self.config['training']['mode'] == 'mixed':
                for loader in self.train_loaders:
                    for batch in tqdm(loader):
                        self.training_step(batch)
            else:
                for batch in tqdm(self.train_loader):
                    self.training_step(batch)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', default='test', choices=['train', 'test'])
    parser.add_argument('--config', default='configs/default.yaml')
    parser.add_argument('--text', help='输入的文本描述')
    parser.add_argument('--output', help='输出路径')
    parser.add_argument('--time', type=float, help='指定的时刻(仅用于图像生成)')
    parser.add_argument('--camera', help='相机视角名称或位置(x,y,z)')
    args = parser.parse_args()
    
    # 加载配置
    config = load_config(args.config)
    
    if args.mode == 'train':
        trainer = WSTrainer(config)
        trainer.train()
    else:
        # 测试模式
        converter = Text2WSF(config)
        
        # 解析相机参数
        if args.camera:
            if ',' in args.camera:
                # 解析为位置坐标
                camera = tuple(map(float, args.camera.split(',')))
            else:
                # 使用预定义视角
                camera = args.camera
        else:
            camera = None
            
        # 生成输出
        if config['generation']['mode'] == 'image':
            # 单帧图像生成
            image = converter.generate_wsf(
                args.text,
                mode='image',
                t=args.time,
                camera=camera
            )
            
            # 保存图像
            if args.output:
                cv2.imwrite(args.output, image)
            
        else:
            # 视频生成
            frames = converter.generate_wsf(
                args.text,
                mode='video',
                camera=camera
            )
            
            # 保存视频
            if args.output:
                save_video(
                    frames,
                    args.output,
                    fps=config['generation']['time']['fps']
                )

if __name__ == "__main__":
    # 使用示例:
    # 1. 训练模式
    # python main.py --mode train --config configs/default.yaml
    
    # 2. 生成单张图像
    # python main.py --mode test --text "一个红色的立方体在桌子上" --output output.wsg --time 0.0 --camera front
    
    # 3. 生成视频
    # python main.py --mode test --text "一个旋转的红色立方体在桌子上" --output output.wsv --camera front
    
    main()