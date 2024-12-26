# World Snapshot Graphics (WSG) Format Specification
Version: 1.0
Last Updated: 2024-12-25

## Overview
WSG (World Snapshot Graphics) is a high-dimensional image format that extends traditional RGB images with additional channels to store rich metadata at the pixel level. Each pixel in a WSG file contains 256 channels of floating-point data.

## Format Core Domain [0-31]
### File Format Information [0-7]
- 0: Format identifier (1919250.0)
- 1: Major version number
- 2: Minor version number
- 3: Patch version number
- 4: Creation timestamp
- 5: Last modification timestamp
- 6: Checksum value
- 7: Flag bits

### Basic Visual [8-15]
- 8: Red component (0-255, float)
- 9: Green component (0-255, float)
- 10: Blue component (0-255, float)
- 11: Alpha value (0-1.0)
- 12: Color space identifier
- 13: Bit depth
- 14: Image quality score
- 15: Compression level

### Core Extension [16-31]
Reserved for core information expansion

## Depth and Geometry Domain [32-63]
### Basic Depth [32-39]
- 32: Absolute depth value (meters)
- 33: Relative depth value (0-1)
- 34: Depth confidence
- 35-37: Surface normal vector (X,Y,Z)
- 38: Curvature
- 39: Edge distance

### Geometry Extension [40-63]
Reserved for depth and geometry expansion

## Pose and Human Information Domain [64-95]
### Basic DWPose Information [64-71]
- 64: Keypoint ID (0-193)
- 65: Person ID
- 66: Confidence
- 67-69: 3D position
- 70: Visibility
- 71: Pose type

### Pose Extension [72-95]
Reserved for pose recognition expansion

## Material Properties Domain [96-127]
### Basic Material [96-103]
- 96: Roughness (0-1)
- 97: Metallic (0-1)
- 98: Specular reflectance
- 99: Transparency
- 100: Refractive index
- 101: Emissive intensity
- 102: Material ID
- 103: Material confidence

### Material Extension [104-127]
Reserved for material properties expansion

## Sound Properties Domain [128-159]
### Global Audio [128-135]
- 128: Main sound pressure level (dB)
- 129: Primary frequency
- 130: Sound source type ID
- 131: Audio event ID
- 132: Basic reverb value
- 133-135: Reserved

### Spatial Audio [136-143]
- 136: Sound attenuation coefficient
- 137: Directional intensity
- 138: Source correlation
- 139-143: Reserved for future spatial audio technologies

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