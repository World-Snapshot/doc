import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class MultiScaleWaveFunction:
    def __init__(self, config):
        self.config = config
        self.scales = config["wave_field"].get("scales", [1.0])
        self.scale_weights = config["wave_field"].get("scale_weights", [1.0])
        
    def schrodinger_wave(self, x, y, k, omega, scale, t=0):
        """多尺度薛定谔波函数"""
        r = torch.sqrt((x*scale)**2 + (y*scale)**2)
        phase = k * r - omega * t
        psi = torch.exp(1j * phase) / torch.sqrt(r + 1e-6)
        return psi
        
    def superposition(self, x, y, params, t=0):
        """多尺度量子态叠加"""
        waves = []
        for scale, weight in zip(self.scales, self.scale_weights):
            scale_waves = []
            for k, omega, amplitude in params:
                wave = self.schrodinger_wave(x, y, k, omega, scale, t)
                scale_waves.append(amplitude * wave)
            waves.append(weight * sum(scale_waves))
        return sum(waves)

class ProbabilityGenerator:
    def __init__(self, config):
        self.target_density = config["grid"].get("target_density", 0.25)
        self.threshold = config["grid"].get("prob_threshold", 0.5)
        
    def get_pixel_mask(self, features, training=True):
        """根据特征生成像素概率掩码"""
        feature_intensity = torch.mean(torch.abs(features), dim=1, keepdim=True)
        prob = torch.sigmoid(feature_intensity)
        
        if training:
            # 训练时使用随机采样
            mask = torch.bernoulli(prob)
        else:
            # 推理时使用阈值
            mask = (prob > self.threshold).float()
            
        return mask, prob

class QuantumWaveGenerator(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.quantum_wave = MultiScaleWaveFunction(config)
        self.prob_generator = ProbabilityGenerator(config)
        
        # 波函数参数生成器
        num_scales = len(config["wave_field"].get("scales", [1.0]))
        self.param_net = nn.Sequential(
            nn.Linear(768, 256),
            nn.ReLU(),
            nn.Linear(256, 9 * num_scales)  # 每个尺度3组参数
        )
        
        # 特征提取器
        self.feature_net = nn.Sequential(
            nn.Linear(4, 64),  # 实部、虚部、振幅、相位
            nn.ReLU(),
            nn.Linear(64, 32)
        )
        
        # 像素生成器
        self.pixel_net = nn.Sequential(
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 4, 1)  # RGB + 概率
        )
        
    def get_wave_params(self, text_embedding):
        params = self.param_net(text_embedding)
        num_scales = len(self.config["wave_field"].get("scales", [1.0]))
        return params.view(-1, num_scales, 3, 3)
        
    def forward(self, text_embedding, coords, t=0):
        batch_size = text_embedding.shape[0]
        h = w = int(coords.shape[1] ** 0.5)
        x, y = coords[..., 0], coords[..., 1]
        
        # 1. 生成波函数参数
        wave_params = self.get_wave_params(text_embedding)
        
        # 2. 计算多尺度量子波函数
        psi_list = []
        for b in range(batch_size):
            params = [(k, o, a) for k, o, a in wave_params[b].reshape(-1, 3)]
            psi = self.quantum_wave.superposition(x[b], y[b], params, t)
            psi_list.append(psi)
        psi = torch.stack(psi_list)
        
        # 3. 提取波函数特征
        wave_features = torch.stack([
            psi.real, psi.imag,
            torch.abs(psi), torch.angle(psi)
        ], dim=-1)
        
        # 4. 生成特征图
        features = self.feature_net(wave_features)
        feature_map = features.view(batch_size, h, w, -1).permute(0, 3, 1, 2)
        
        # 5. 生成像素和概率
        outputs = self.pixel_net(feature_map)
        rgb = torch.sigmoid(outputs[:, :3])  # RGB
        prob_logits = outputs[:, 3:]  # 概率logits
        
        # 6. 生成概率掩码
        mask, prob = self.prob_generator.get_pixel_mask(
            prob_logits, 
            self.training
        )
        
        return rgb * mask, prob, psi

class QuantumLoss(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        
    def forward(self, rgb, prob, psi, target_images):
        losses = {}
        
        # 1. 实像素重建损失
        losses['rgb'] = F.mse_loss(rgb, target_images) * \
                       self.config["loss"]["real_weight"]
        
        # 2. 概率密度损失
        target_density = self.config["grid"]["target_density"]
        losses['density'] = F.mse_loss(
            prob.mean(), 
            torch.tensor(target_density).to(prob.device)
        ) * self.config["loss"].get("density_weight", 0.1)
        
        # 3. 波函数概率密度损失
        prob_density = torch.abs(psi)**2
        target_density = (target_images.mean(dim=1) + 1) / 2
        losses['quantum'] = F.mse_loss(
            prob_density, 
            target_density
        ) * self.config["loss"]["quantum_weight"]
        
        # 4. 连续性损失
        grad_psi = torch.gradient(psi, dim=(-2, -1))[0]
        losses['continuity'] = torch.mean(
            torch.abs(grad_psi)
        ) * self.config["loss"]["continuity_weight"]
        
        return sum(losses.values()), losses

if __name__ == "__main__":
    config = {
        "wave_field": {
            "enabled": True,
            "strength": 1.0,
            "scales": [0.5, 1.0, 2.0],  # 多尺度配置
            "scale_weights": [0.3, 1.0, 0.5]  # 各尺度权重
        },
        "grid": {
            "target_density": 0.25,  # 目标像素密度
            "prob_threshold": 0.5,   # 概率阈值
        },
        "loss": {
            "real_weight": 1.0,
            "quantum_weight": 0.1,
            "continuity_weight": 0.05,
            "density_weight": 0.1
        }
    }
    
    model = QuantumWaveGenerator(config)
    
    # 示例输入
    text_embedding = torch.randn(1, 768)
    coords = torch.randn(1, 64*64, 2)
    
    # 生成图像
    rgb, prob, psi = model(text_embedding, coords)