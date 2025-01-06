# World Snapshot Graphics (WSG) Format Specification
Version: 1.0
Last Updated: 2024-12-25

## Overview
WSG (World Snapshot Graphics) is a high-dimensional image format that extends traditional RGB images with additional channels to store rich metadata at the pixel level. Each pixel in a WSG file contains 256 channels of floating-point data.

## Format Core Domain [0-31]
### Essential Visual [0-7]
- 0: Red component (0-255, float)
- 1: Green component (0-255, float)
- 2: Blue component (0-255, float)
- 3: Alpha value (0-1.0)
- 4: Reserved for future essential
- 5: Reserved for future essential
- 6: Reserved for future essential
- 7: Reserved for future essential

### Quantum Phase Field [8-15] (必需)
- 8: Phase value (0-1) - 像素状态叠加表示
- 9: Gradient magnitude - 状态转换梯度强度 
- 10: Direction field - 8方向编码
- 11: Pixel flags (实/虚像素标记)
- 12: Quantum state confidence
- 13-15: Reserved for quantum properties

### Core Extension [16-31] (必需)
- 16: Color space identifier
- 17: Bit depth
- 18: Image quality score
- 19: Compression level
- 20-31: Reserved for core information expansion

## Depth and Geometry Domain [32-63]
### Basic Depth [32-39] (必需 - 可通过深度估计获取)
- 32: Absolute depth value (meters)
- 33: Relative depth value (0-1)
- 34: Depth confidence
- 35-37: Surface normal vector (X,Y,Z)
- 38: Curvature
- 39: Edge distance

### Advanced Geometry [40-47] (可选 - AI推断)
- 40: Surface roughness map
- 41: Displacement map
- 42: Ambient occlusion
- 43: Geometric detail level
- 44: Surface continuity
- 45-47: Reserved for geometry details

### Motion Geometry [48-55] (必需 - 从视频提取)
- 48: Motion vector X
- 49: Motion vector Y
- 50: Motion vector Z
- 51: Deformation gradient
- 52: Motion blur factor
- 53: Temporal consistency weight
- 54-55: Reserved for motion data

### Geometry Extension [56-63]
Reserved for future geometry data

## Pose and Human Information Domain [64-95]
### Basic DWPose Information [64-71] (可选 - 通过姿态估计)
- 64: Keypoint ID (0-193)
- 65: Person ID
- 66: Confidence
- 67-69: 3D position
- 70: Visibility
- 71: Pose type

### Advanced Pose [72-79] (可选 - AI推断)
- 72: Joint rotations
- 73: Action class ID
- 74: Movement speed
- 75: Interaction ID
- 76-79: Reserved for pose dynamics

### Physics Properties [80-87] (可选 - 物理推断)
- 80: Mass estimation
- 81: Center of gravity
- 82: Basic collision bounds
- 83: Object rigidity
- 84-87: Reserved for physics

### Pose Extension [88-95]
Reserved for future pose data

## Material Properties Domain [96-127]
### Basic Material [96-103] (可选 - 材质估计)
- 96: Roughness (0-1)
- 97: Metallic (0-1)
- 98: Specular reflectance
- 99: Transparency
- 100: Refractive index
- 101: Emissive intensity
- 102: Material ID
- 103: Material confidence

### Advanced Material [104-111] (可选 - 高级材质推断)
- 104: Subsurface scattering
- 105: Anisotropic roughness
- 106: Clearcoat
- 107: Sheen
- 108: Iridescence
- 109-111: Reserved for material properties

### Material Attributes [112-119] (可选 - 视觉属性)
- 112: Surface age/wear
- 113: Weathering pattern
- 114: Surface temperature (visual)
- 115-119: Reserved for visual attributes

### Material Extension [120-127]
Reserved for future material properties

## Sound Properties Domain [128-159]
### Global Audio [128-135] (必需 - 音频分析)
- 128: Sound pressure level (dB)
- 129: Primary frequency
- 130: Sound source type ID
- 131: Audio event ID
- 132: Basic reverb value
- 133-135: Reserved

### Spatial Audio [136-143] (可选 - 空间音频分析)
- 136: Sound attenuation
- 137: Directional intensity
- 138: Source correlation
- 139: Room acoustics estimate
- 140: Doppler effect
- 141-143: Reserved

### Audio Analysis [144-151] (可选 - AI音频分析)
- 144: Harmonic content
- 145: Audio texture
- 146: Emotional valence
- 147: Scene audio class
- 148: Background noise level
- 149-151: Reserved

### Audio Extension [152-159]
Reserved for future audio properties

## Technical Details

### Data Types
- All channels use 32-bit floating point values (float32)
- Special values:
 - NaN: Invalid/missing data
 - ∞: Unlimited/maximum value
 - -∞: Minimum value

### Channel Values Storage
- All numerical values should be stored in their natural units  
- Normalized values should be stored in 0-1 range
- IDs should be stored as integers
- Confidence values should be stored in 0-1 range

### Version Control
Version format: MAJOR.MINOR.PATCH
- MAJOR: Breaking changes
- MINOR: New features, backward compatible 
- PATCH: Bug fixes, backward compatible

### File Structure
- Binary format
- Channels can be stored in either interleaved or planar format
- Optional lossless compression support
- First three channels (RGB) must always be valid

### Compatibility Requirements
- Applications must gracefully handle missing channel data
- RGB channels must remain viewable in standard image viewers
- Channel expansion must maintain backward compatibility

## Best Practices

### Data Population
- Only populate channels with meaningful data
- Use NaN for unknown values
- Maintain consistent units across all files

### Implementation Guidelines
- Validate channel ranges before saving
- Ensure RGB channels remain viewable
- Preserve aspect ratio and resolution
- Use appropriate compression for large datasets
- Consider streaming access for large files
- Cache frequently accessed channels

## Core Concepts Notes

### Original Concept
1. Grid Structure
- 3x3 pixel grid arrangement
- Center pixel is real, surrounding 8 pixels are virtual
- Virtual pixels represent quantum probability states
- Aims to reduce computation to 1/9 while maintaining quality

2. Quantum Approach
- Each virtual pixel represents potential state transitions
- Probabilistic distribution similar to quantum mechanics
- Allows for efficient representation of complex states
- Supports differentiable computations

### Implementation Strategy
1. Phase Field Design
- Phase value represents pixel state superposition
- Gradient field describes transition tendencies
- Direction field encodes 8-neighborhood information
- Flags distinguish between real and virtual pixels

2. Architecture Benefits
- Combines 3DGS efficiency
- Maintains NeRF continuity
- Reduces computational complexity through quantization
- Enables differentiable operations

### Development Roadmap
1. Core Development
- Design training strategy
- Implement loss functions
- Optimize probability field calculations
- Validate performance improvements

2. Technical Validation
- Benchmark computation reduction
- Verify quality preservation
- Test differentiability
- Measure memory efficiency

3. Advanced Features
- Multi-resolution support
- Temporal coherence
- Adaptive sampling
- Hardware acceleration

### Research Directions
1. Training Methods
- Design specialized loss functions
- Develop efficient training strategies
- Optimize convergence rates

2. Optimization Techniques
- Probability field optimization
- Quantum state representation
- Performance enhancement methods

3. Validation Metrics
- Quality assessment methods
- Performance benchmarks
- Compatibility testing