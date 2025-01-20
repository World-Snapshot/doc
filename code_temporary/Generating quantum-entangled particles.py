class EntangledWaveFunction:
    """处理纠缠态的波函数"""
    def __init__(self):
        self.entangled_pairs = {}  # 存储纠缠对
        
    def create_bell_state(self, id1, id2, state_type='phi_plus'):
        """创建Bell态纠缠对"""
        # 创建标准Bell态
        if state_type == 'phi_plus':
            # |φ+⟩ = (|00⟩ + |11⟩)/√2
            state = torch.tensor([1.0, 0.0, 0.0, 1.0]) / np.sqrt(2)
        elif state_type == 'phi_minus':
            # |φ-⟩ = (|00⟩ - |11⟩)/√2
            state = torch.tensor([1.0, 0.0, 0.0, -1.0]) / np.sqrt(2)
        elif state_type == 'psi_plus':
            # |ψ+⟩ = (|01⟩ + |10⟩)/√2
            state = torch.tensor([0.0, 1.0, 1.0, 0.0]) / np.sqrt(2)
        else:  # psi_minus
            # |ψ-⟩ = (|01⟩ - |10⟩)/√2
            state = torch.tensor([0.0, 1.0, -1.0, 0.0]) / np.sqrt(2)
            
        self.entangled_pairs[(id1, id2)] = {
            'state': state,
            'measured': False
        }
        
    def measure_particle(self, particle_id, basis='computational'):
        """测量一个粒子的状态"""
        # 找到包含该粒子的纠缠对
        pair = None
        other_particle = None
        for (id1, id2), state_info in self.entangled_pairs.items():
            if particle_id in (id1, id2):
                pair = (id1, id2)
                other_particle = id2 if particle_id == id1 else id1
                break
                
        if pair is None:
            raise ValueError(f"Particle {particle_id} not found in any entangled pair")
            
        if self.entangled_pairs[pair]['measured']:
            raise ValueError("This entangled pair has already been measured")
            
        # 进行测量
        state = self.entangled_pairs[pair]['state']
        if basis == 'computational':
            # 在计算基下测量
            probs = torch.abs(state)**2
            result = torch.multinomial(probs, 1).item()
            
            # 根据测量结果确定另一个粒子的状态
            if result in [0, 3]:  # |00⟩ or |11⟩
                other_result = result
            else:  # |01⟩ or |10⟩
                other_result = 1 if result == 2 else 2
                
            self.entangled_pairs[pair]['measured'] = True
            
            return result, other_result
            
        # 可以添加其他测量基底的实现
        
    def get_entangled_state(self, particle_id):
        """获取粒子的纠缠状态"""
        for (id1, id2), state_info in self.entangled_pairs.items():
            if particle_id in (id1, id2):
                return state_info['state']
        return None

class EntangledWSF(WSF):
    """支持量子纠缠的WSF"""
    def __init__(self, config):
        super().__init__(config)
        self.entangled_wave = EntangledWaveFunction()
        
    def create_entangled_views(self, view_id1, view_id2, state_type='phi_plus'):
        """创建纠缠的视图对"""
        self.entangled_wave.create_bell_state(view_id1, view_id2, state_type)
        
    def compute_quantum_superposition(self, point):
        """考虑纠缠态的量子叠加"""
        psi_total = 0
        weights = 0
        
        # 检查是否有纠缠态
        for view_id, quantum_state in self.views.items():
            entangled_state = self.entangled_wave.get_entangled_state(view_id)
            
            if entangled_state is not None:
                # 使用纠缠态修改波函数
                camera = self.camera_params[view_id]
                weight = self.compute_view_weight(point, camera)
                
                # 获取基础波函数
                psi_base = self.quantum_wave.evaluate_3d(
                    point,
                    quantum_state.wave_params,
                    quantum_state.t
                )
                
                # 将纠缠态整合到波函数中
                psi = self.apply_entanglement(psi_base, entangled_state)
                
                psi_total += weight * psi
                weights += weight
            else:
                # 非纠缠态的正常处理
                camera = self.camera_params[view_id]
                weight = self.compute_view_weight(point, camera)
                
                psi = self.quantum_wave.evaluate_3d(
                    point,
                    quantum_state.wave_params,
                    quantum_state.t
                )
                
                psi_total += weight * psi
                weights += weight
        
        if weights > 0:
            psi_total /= torch.sqrt(weights)
            
        return psi_total
        
    def apply_entanglement(self, psi_base, entangled_state):
        """将纠缠态应用到基础波函数"""
        # 将基础波函数分解为两个分量
        psi_0 = psi_base * entangled_state[0]  # |0⟩分量
        psi_1 = psi_base * entangled_state[1]  # |1⟩分量
        
        # 构建纠缠波函数
        psi_entangled = psi_0 + psi_1
        
        return psi_entangled
    

# USAGE:

# 创建支持纠缠的WSF
wsf = EntangledWSF(config)

# 创建纠缠的视图对
wsf.create_entangled_views(view_id1=0, view_id2=1, state_type='phi_plus')

# 后续操作和原来一样
wsf.merge_views()