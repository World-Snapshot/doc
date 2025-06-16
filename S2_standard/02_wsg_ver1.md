# World Snapshot Graphics (WSG) Format Specification
Version: 1.0;
Draft was established on: 2024-12-25;
Last Updated: 2025-06-15;
History Version at <a href="https://github.com/World-Snapshot/doc/commits/main/" target="_blank">link</a>

## Overview
WSG (World Snapshot Graphics) is a high-dimensional image format that extends traditional RGB images with additional channels to store rich metadata at the pixel level. Each pixel in a WSG file contains 256 channels of floating-point data.

Generally speaking:

1. I set -1 as the mask area, representing non-existence. 0 represents False, and 1 represents existence or True. WSG should be able to be read and trained in the NPZ format, as this is the most common format for AI and it has a strong compression capability for repeat number (eg., -1.)
2. The indentation relationship represents the loop/subordinate relationship.
3. Regarding the optional format standards, we have not conducted in-depth trials and do not have corresponding WSG file samples. They are merely recommended. We may calibrate them in future WSG minor version updates.

## Format Core Domain [0-31]
### Essential Visual [0-7] (Necessary)
- 0: Red component (0-255, float)
- 1: Green component (0-255, float)
- 2: Blue component (0-255, float)
- 3: Alpha value (0-1.0)
- 4: Reserved for future essential
- 5: Reserved for future essential
- 6: Reserved for future essential
- 7: Reserved for future essential

**Note:** Our training process involves combining the 3/4 channel images initialized by the Sen Fang wave with the remaining 200+ valid information, and then predicting the RGB + 253 channels. We hope to learn during this process how to control the 253 types of conditional information, such as space, existence, and the operation of the world, as well as how these conditional information can be inferred from each other.

### Quantum Phase Field [8-15] (Necessary) (Encodable control domain)
- 8: Phase value (0-1) - 像素状态叠加表示
- 9: Gradient magnitude - 状态转换梯度强度 
- 10: Direction field - 8方向编码
- 11: Pixel flags (实/虚像素标记)
- 12: Quantum state confidence
- 13-15: Reserved for quantum properties

**Note:** Initially, I planned to encode some information into the frequency of the wave using the frequency modulation method. This way, we wouldn't need the additional 253 channels for initialization, and the information would be closely integrated with the wave. However, 1. We ourselves need to initialize a tensor that is the same as the expected output result. At least after our reverse reasoning, we still have 256 channels. 2. If we want to change the results of the bidirectional reasoning more quickly, it would be best if we could directly input and directly modify the specific values that have not been encoded. 3. Placing the initialization information of the wave (instead of the function solution, the solution should be initialized and placed in the first four channels) into the additional channels helps us to reconstruct the wave world. 4. Encoding all the information into Wave itself will make Wave Encoder might be very difficult to train. We not only increased the burden on the Wave generator, but also increased the burden on the pixel decoder. 5. But, the drawback of new method (The method of placing all the information into an additional channel) is that 3D information is transformed into 2D information, which is prone to being obscured and confused, and it is difficult to handle the changes after interaction. Therefore, I plan to encode some invariant quantities into the waves as a double safeguard.

**Note:** For the time being, I have only designated this one domain as being capable of being encoded, because other information is not generated along with the wave function. If the wave core space is not clean, you cannot accurately encode the corresponding properties into specific waves; artificial contamination will occur.

### Core Extension [16-31] (Optional)
- 16: Color space identifier
- 17: Bit depth
- 18: Image quality score
- 19: Compression level
- 20-31: Reserved for core information expansion

## Depth and Geometry Domain [32-63]
### Basic Depth [32-40] (Necessary)
- 32: Absolute depth value (meters)
- 33: Absolute depth confidence (In fact, only a very small number of jobs offer this, and we are not using it for the time being.)
- 34: Relative depth value (0-1)
- 35: Relative depth confidence (In fact, only a very small number of jobs offer this, and we are not using it for the time being.)
- 36-38: Surface normal vector (X,Y,Z)
- 39: Curvature (For a sphere, each of its positions has a curvature. It's somewhat like the 3D version of a boundary.)
- 40: Edge （False -1, True 1; -1 indicates the area of the mask, and this area is not taken into consideration at all.）

### Advanced Geometry [41-48] (Optional)
- 41: Surface roughness map
- 42: Displacement map
- 43: Ambient occlusion
- 44: Geometric detail level
- 45: Surface continuity
- 46-48: Reserved for geometry details

### Motion Geometry [49-56] (Optional)
- 49: Motion vector X
- 50: Motion vector Y
- 51: Motion vector Z
- 52: Deformation gradient
- 53: Motion blur factor
- 54: Temporal consistency weight
- 55-56: Reserved for motion data

### Geometry Extension [57-63]
Reserved for future geometry data

## Pose and Human Information Domain [64-95]
### 2D skeletal human (DWPose) [64-71] (Necessary)
- 64: Person ID (-1 or ID number)
    - 65: Keypoint ID (about 0-134, find this keypoint based on the xy coordinates, and then mark which key point it is.)
        - 66: Score (The body score serves as an index. One person occupies 18 index values, and then the second person increments. The remaining scores represent the degree of confidence.)
- 67-71: Reserved for future 2D skeletal pose data

**Note:** The design principle for 2D skeleton poses is to define the key point ID channels, then find the corresponding pixels for the key points, and set the corresponding channels to 1/Ture. In this way, when we detect a true channel, we know that there is a key point at that location, and then we know which key point it is.

### 3D mesh human (SMPLer-X) [72-94] (Necessary)
- 72: Person ID (from bbox_id in meta dir)
    - 73: Joint ID (global_orient + left_hand_pose + right_hand_pose + jaw_pose + leye_pose + reye_pose + transl)
        - 74: Joint rotations or transl x
        - 75: Joint rotations or transl y
        - 76: Joint rotations or transl z
- 77: betas: 0 epression: 1
    - 78-87: the value of betas/epression
- 88: bbox: If the vertex is set to 1, then the absence of a vertex is naturally -1.
- 89: bbox_mmdet: If the vertex is set to 1, then the absence of a vertex is naturally -1.
- 90: vertices (vf system): If the vertex is set to 1, then the absence of a vertex is naturally -1.
- 91-94: Reserved for future

**Note:** I utilized the bbox_mmdet and bbox information from Meta dir, but did not use focal and princpt, as these two elements will be provided by user.

**Note:** For 3D Mesh human models, each joint has a rotation angle. Then we use keypoint ID plus xyz rotation angles, and four channels can store this information. However, since the rotation angles do not reflect the spatial information in the image, we cannot find the corresponding pixels. We can only store this information for each pixel in the entire human body area. (This allows the model to have some sensitivity to the human body area and the large amount of information enrichment is also helpful for the already difficult 3D posture training.) If the positions of people overlap, the pixel area of this part should be given to the person with the smaller ID because this is the person that the model is most likely to detect first.

**Note:** The final rendering mainly uses the bbox (SMPLer-X box), while bbox_mmdet seems to represent smaller body areas. When saving, I should use the bbox box. Additionally, I did not store the face meshes because for SMPL, the connection relationship of its face meshes is fixed.

### 3D skeletal human (Mediapipe Pose) [95-102] (Necessary)

- 95: Person ID (-1 or ID number)
    - 96: Joint ID (Find this keypoint based on the xy coordinates, and then mark which key point it is.)
        - 97: z: relative depth: Positive values indicate proximity to the camera, while negative values indicate distance from the camera.
        - 98: Visibility confident

- 99-102: Reserved for future

### Human segmentation (Sapiens) [103-110] (Optional)

- 103-110: Reserved for future

## Physics Properties Domain [80-95]
### Basic Physics [80-87] (Necessary)

- 80: Mass distribution (relative, 0-1)
```
- 0: extremely light
- 1: extremely heavy
- NaN: unknown
```

- 81: Center of gravity (3D coordinates, normalized)
```
- Vector3(x,y,z) relative to pixel position
- NaN: unknown
```

- 82: Basic collision bounds
```
- Bit flags for collision shape primitives
- 0x01: sphere
- 0x02: box
- 0x04: capsule
- 0x08: mesh
```

- 83: Object rigidity (0-1)
```
- 0: completely soft
- 1: completely rigid
- Derived from Young's modulus
```

### Advanced Physics [84-95] (Optional)
- 84: Material density (relative, 0-1)
```
- Local density at pixel position
- Normalized relative to standard density table
```

- 85: Young's modulus (normalized, 0-1)
```
- Local elasticity at pixel position
- Mapped from standard material values
```

- 86: Poisson ratio (0-0.5)
```
- Local deformation property
- NaN if not applicable
```

- 87: Friction coefficient (0-1)
```
- Surface friction property
- NaN if not applicable
```

- 88: Restitution coefficient (0-1)
```
- Bounce/energy retention
- NaN if not applicable
```

- 89-95: Reserved for future physics properties

## Material Properties Domain [96-127]
### Basic Material [96-103] (Optional - 材质估计)
- 96: Roughness (0-1)
```
- Surface roughness value
- NaN if not measurable
```

- 97: Metallic (0-1)
```
- Metallic property value
- Higher values indicate more metallic properties
```

- 98: Specular reflectance
```
- Surface light reflection characteristics
- Based on material properties
```

- 99: Transparency
```
- Material transparency level
- 0: completely opaque
- 1: completely transparent
```

- 100: Refractive index
```
- Material's light bending properties
- Standard range: 1.0-3.0
```

- 101: Emissive intensity
```
- Self-illumination strength
- 0: no emission
```

- 102: Material ID
```
- Reference to material database
- Unique identifier for each material type
```

- 103: Material confidence
```
- Confidence in material classification
- 0-1 range
```

### Material Classification [104-127] (Optional)
- 104: Material type
```
- Basic material classification
- 0x01: solid
- 0x02: liquid
- 0x04: granular
```

### Material Extension [105-127]
Reserved for future material properties

## Sound Properties Domain [128-159]
### Global Audio [128-135] (Necessary - 音频分析)
- 128: Sound pressure level (dB)
- 129: Primary frequency
- 130: Sound source type ID
- 131: Audio event ID
- 132: Basic reverb value
- 133-135: Reserved

### Spatial Audio [136-143] (Optional - 空间音频分析)
- 136: Sound attenuation
- 137: Directional intensity
- 138: Source correlation
- 139: Room acoustics estimate
- 140: Doppler effect
- 141-143: Reserved

### Audio Analysis [144-151] (Optional - AI音频分析)
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

*Please read blogs "01 Rethink Best Papers" and "02 Computer Vision's Rebirth"*