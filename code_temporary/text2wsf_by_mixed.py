import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from transformers import AutoTokenizer, AutoModel
from diffusers import UNet2DModel, DDPMScheduler
from text2wsg import Text2WSG, WSG  # 导入WSG相关代码

class CameraParams:
    def __init__(self, position, rotation, fov=60):
        self.position = np.array(position)  # (x, y, z)
        self.rotation = np.array(rotation)  # (pitch, yaw, roll)
        self.fov = fov
        self.compute_matrices()
    
    def compute_matrices(self):
        """计算相机矩阵"""
        # 简化版本，实际应用需要完整的相机矩阵计算
        self.view_matrix = np.eye(4)
        self.projection_matrix = np.eye(4)

class WSF:
    """World Snapshot Field"""
    def __init__(self):
        self.views = {}  # 存储多个视角的WSG
        self.camera_params = {}  # 存储相机参数
        self.unified_field = None  # 统一的3D场表示
        
    def add_view(self, view_id, wsg, camera_params):
        """添加新的视角"""
        self.views[view_id] = wsg
        self.camera_params[view_id] = camera_params
    
    def compute_view_weight(self, point, camera_params):
        """计算视角权重"""
        # 基于点到相机的距离和角度计算权重
        distance = np.linalg.norm(point - camera_params.position)
        return 1.0 / (distance + 1e-6)
    
    def merge_views(self):
        """合并多个视角信息"""
        if not self.views:
            return
        
        # 1. 确定统一场的范围
        self.determine_field_bounds()
        
        # 2. 对每个空间点，融合所有视角的信息
        for point in self.get_field_points():
            merged_state = self.merge_point_states(point)
            self.set_field_state(point, merged_state)
    
    def determine_field_bounds(self):
        """确定场的边界"""
        # 根据所有视角的覆盖范围确定边界
        # 这里使用简化版本
        self.bounds = {
            'min': np.array([-1, -1, -1]),
            'max': np.array([1, 1, 1])
        }
    
    def get_field_points(self):
        """获取场中的采样点"""
        # 简化版本，返回网格点
        x = np.linspace(self.bounds['min'][0], self.bounds['max'][0], 32)
        y = np.linspace(self.bounds['min'][1], self.bounds['max'][1], 32)
        z = np.linspace(self.bounds['min'][2], self.bounds['max'][2], 32)
        return np.meshgrid(x, y, z)
    
    def merge_point_states(self, point):
        """合并某点的所有视角状态"""
        merged_state = np.zeros(160)  # WSG状态维度
        total_weight = 0
        
        for view_id, wsg in self.views.items():
            camera = self.camera_params[view_id]
            weight = self.compute_view_weight(point, camera)
            
            # 创建相机参数
            rotation = self.compute_camera_rotation(pos)
            camera = CameraParams(pos, rotation)
            
            views[view_id] = wsg
            camera_params[view_id] = camera
            
        return views, camera_params
    
    def compute_camera_rotation(self, position):
        """计算相机旋转以面向原点"""
        # 简化版本：假设相机总是朝向原点
        direction = -position  # 指向原点的向量
        
        # 计算俯仰角和偏航角
        pitch = np.arctan2(direction[1], np.sqrt(direction[0]**2 + direction[2]**2))
        yaw = np.arctan2(-direction[0], -direction[2])
        
        return np.array([pitch, yaw, 0])  # roll设为0
    
    def generate_wsf(self, text, camera_positions):
        """生成WSF"""
        # 1. 创建WSF对象
        wsf = WSF()
        
        # 2. 生成多个视角的WSG
        views, camera_params = self.generate_views(text, camera_positions)
        
        # 3. 添加视角到WSF
        for view_id in views:
            wsf.add_view(view_id, views[view_id], camera_params[view_id])
        
        # 4. 合并视角
        wsf.merge_views()
        
        return wsf

# 使用示例
def main():
    # 创建转换器
    converter = Text2WSF()
    
    # 定义相机位置（简化的球面分布）
    radius = 2.0
    camera_positions = [
        (0, 0, radius),      # 正面
        (radius, 0, 0),      # 右侧
        (-radius, 0, 0),     # 左侧
        (0, radius, 0),      # 顶部
        (0, -radius, 0),     # 底部
        (0, 0, -radius)      # 背面
    ]
    
    # 生成WSF
    text = "一个红色的立方体在桌子上"
    wsf = converter.generate_wsf(text, camera_positions)
    
    # 检查结果
    print("WSF generation completed")
    print(f"Number of views: {len(wsf.views)}")
    print(f"Field shape: {wsf.unified_field.shape}")

if __name__ == "__main__":
    main() 投影点到视角的WSG
            projected_state = self.project_point_to_view(point, wsg, camera)
            
            # 加权累加
            merged_state += weight * projected_state
            total_weight += weight
        
        if total_weight > 0:
            merged_state /= total_weight
            
        return merged_state
    
    def project_point_to_view(self, point, wsg, camera):
        """将3D点投影到特定视角的WSG"""
        # 1. 世界坐标到相机坐标
        point_camera = np.linalg.inv(camera.view_matrix) @ np.append(point, 1)
        
        # 2. 相机坐标到图像坐标
        point_image = camera.projection_matrix @ point_camera
        point_image = point_image[:2] / point_image[2]
        
        # 3. 获取最近的WSG像素
        x = int(point_image[0] * wsg.width)
        y = int(point_image[1] * wsg.height)
        x = np.clip(x, 0, wsg.width - 1)
        y = np.clip(y, 0, wsg.height - 1)
        
        return wsg.pixels[(x, y)].state.properties
    
    def set_field_state(self, point, state):
        """设置场中某点的状态"""
        if self.unified_field is None:
            self.initialize_unified_field()
        
        # 将点坐标转换为场的索引
        indices = self.point_to_indices(point)
        self.unified_field[indices] = state
    
    def initialize_unified_field(self):
        """初始化统一场"""
        field_shape = (32, 32, 32, 160)  # 简化版本使用固定大小
        self.unified_field = np.zeros(field_shape)
    
    def point_to_indices(self, point):
        """将空间点转换为场索引"""
        normalized = (point - self.bounds['min']) / (self.bounds['max'] - self.bounds['min'])
        indices = (normalized * np.array([32, 32, 32])).astype(int)
        indices = np.clip(indices, 0, 31)
        return tuple(indices)

class Text2WSF:
    def __init__(self):
        self.text2wsg = Text2WSG()
        
    def generate_views(self, text, camera_positions):
        """生成多个视角的WSG"""
        views = {}
        camera_params = {}
        
        for view_id, pos in enumerate(camera_positions):
            # 为每个视角生成WSG
            wsg = self.text2wsg.generate_wsg(text)
            
            # 创建相机参数
            rotation = self.compute_camera_rotation(pos)
            camera = CameraParams(pos, rotation)
            
            views[view_id] = wsg
            camera_params[view_id] = camera
            
        return views, camera_params
    
    def compute_camera_rotation(self, position):
        """计算相机旋转以面向原点"""
        # 简化版本：假设相机总是朝向原点
        direction = -np.array(position)  # 指向原点的向量
        
        # 计算俯仰角和偏航角
        pitch = np.arctan2(direction[1], np.sqrt(direction[0]**2 + direction[2]**2))
        yaw = np.arctan2(-direction[0], -direction[2])
        
        return np.array([pitch, yaw, 0])  # roll设为0
    
    def apply_view_transform(self, wsg, camera):
        """应用视角变换到WSG"""
        transformed_wsg = WSG(wsg.width, wsg.height)
        
        # 对每个像素应用变换
        for coord, pixel in wsg.pixels.items():
            # 将像素转换到世界坐标
            world_pos = self.pixel_to_world(coord, pixel.coordinate.relative_depth, camera)
            
            # 更新像素信息
            transformed_wsg.pixels[coord].coordinate.relative_depth = world_pos[2]
            transformed_wsg.pixels[coord].state = pixel.state
            
        return transformed_wsg
    
    def pixel_to_world(self, pixel_coord, depth, camera):
        """将像素坐标转换到世界坐标"""
        x, y = pixel_coord
        
        # 归一化像素坐标
        fx = (x / self.text2wsg.generate_wsg("").width - 0.5) * 2
        fy = (y / self.text2wsg.generate_wsg("").height - 0.5) * 2
        
        # 构建相机空间点
        camera_point = np.array([fx, fy, -1]) * depth
        
        # 应用相机变换
        rotation_matrix = self.rotation_matrix_from_angles(camera.rotation)
        world_point = rotation_matrix @ camera_point + camera.position
        
        return world_point
    
    def rotation_matrix_from_angles(self, angles):
        """从欧拉角创建旋转矩阵"""
        pitch, yaw, roll = angles
        
        # 创建基本旋转矩阵（简化版本）
        Rx = np.array([[1, 0, 0],
                      [0, np.cos(pitch), -np.sin(pitch)],
                      [0, np.sin(pitch), np.cos(pitch)]])
                      
        Ry = np.array([[np.cos(yaw), 0, np.sin(yaw)],
                      [0, 1, 0],
                      [-np.sin(yaw), 0, np.cos(yaw)]])
                      
        Rz = np.array([[np.cos(roll), -np.sin(roll), 0],
                      [np.sin(roll), np.cos(roll), 0],
                      [0, 0, 1]])
                      
        return Rz @ Ry @ Rx
    
    def generate_wsf(self, text, camera_positions):
        """生成WSF
        Args:
            text (str): 输入的文本描述
            camera_positions (list): 相机位置列表，每个元素是(x,y,z)元组
        Returns:
            WSF: 生成的World Snapshot Field对象
        """
        # 1. 创建WSF对象
        wsf = WSF()
        
        # 2. 生成多个视角的WSG
        views, camera_params = self.generate_views(text, camera_positions)
        
        # 3. 为每个视角生成深度图
        for view_id in views:
            wsg = views[view_id]
            camera = camera_params[view_id]
            
            # 3.1 应用视角变换以获取正确的深度信息
            transformed_wsg = self.apply_view_transform(wsg, camera)
            
            # 3.2 添加到WSF
            wsf.add_view(view_id, transformed_wsg, camera)
        
        # 4. 合并所有视角信息
        wsf.merge_views()
        
        # 5. 后处理
        # 5.1 检查并填充空洞
        wsf.fill_holes()
        
        # 5.2 平滑过渡
        wsf.smooth_transitions()
        
        # 5.3 优化波函数一致性
        wsf.optimize_wave_consistency()
        
        # 5.4 计算不确定性
        wsf.compute_uncertainty()
        
        return wsf

def fill_holes(self):
    """填充视角合并后可能出现的空洞"""
    if self.unified_field is None:
        return
        
    # 使用3D形态学操作填充空洞
    from scipy import ndimage
    
    # 创建掩码标识空值
    mask = np.any(self.unified_field == 0, axis=-1)
    
    # 对每个状态通道进行填充
    for i in range(self.unified_field.shape[-1]):
        channel = self.unified_field[..., i]
        # 使用最近邻填充
        filled = ndimage.morphology.binary_fill_holes(channel)
        # 更新原始数据
        self.unified_field[..., i] = filled

def smooth_transitions(self):
    """平滑视角之间的过渡"""
    if self.unified_field is None:
        return
        
    # 使用3D高斯滤波进行平滑
    from scipy.ndimage import gaussian_filter
    
    # 对每个状态通道进行平滑
    for i in range(self.unified_field.shape[-1]):
        channel = self.unified_field[..., i]
        # 应用高斯平滑，sigma参数控制平滑程度
        smoothed = gaussian_filter(channel, sigma=1.0)
        self.unified_field[..., i] = smoothed

def optimize_wave_consistency(self):
    """优化波函数一致性"""
    if self.unified_field is None:
        return
        
    # 1. 计算波函数梯度
    gradients = np.gradient(self.unified_field[..., 8])  # 使用相位场
    
    # 2. 标识不连续区域
    discontinuities = np.abs(gradients) > threshold
    
    # 3. 在不连续区域应用局部优化
    for idx in np.argwhere(discontinuities):
        self._optimize_local_wave(idx)

def _optimize_local_wave(self, center_idx):
    """优化局部波函数"""
    # 获取局部区域
    local_region = self._get_local_region(center_idx)
    
    # 计算局部相位一致性
    phase = self.unified_field[..., 8][local_region]
    
    # 应用局部优化
    optimized_phase = self._phase_optimization(phase)
    
    # 更新结果
    self.unified_field[..., 8][local_region] = optimized_phase

def compute_uncertainty(self):
    """计算场中的不确定性"""
    if self.unified_field is None:
        return
        
    # 1. 计算视角覆盖
    coverage = self._compute_view_coverage()
    
    # 2. 评估几何一致性
    geometry_consistency = self._evaluate_geometry_consistency()
    
    # 3. 计算波函数干涉
    wave_interference = self._compute_wave_interference()
    
    # 4. 合并不确定性指标
    self.uncertainty = self._combine_uncertainty_metrics(
        coverage,
        geometry_consistency,
        wave_interference
    )