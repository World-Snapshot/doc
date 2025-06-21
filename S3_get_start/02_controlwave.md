# ControlWave

<!--*"Wave is all things those worlds need."*-->
*"I suspect that waves are the most suitable core of the world." -- SF*

## Overview

ControlWave is a WebUI that makes WaveGen more convenient to control. Unlike [ControlNet](https://github.com/lllyasviel/ControlNet?tab=readme-ov-file), WaveGen natively supports various controls and doesn't require training additional neural blocks like ControlNet does. Therefore, this is just a WebUI.

ControlWave is mainly divided into two parts, one concerning the core space and one concerning the pixel layer. It's like an inner world and an outer world. For ControlWave, first it should have all the basic functions of ControlNet, and then by controlling the core space, it have more amazing capabilities.

**Note1:** Although ControlWave is a WebUI, in this section I will explain its main working principle and incorporate a part of the WaveGen method here. That is, how to control the wave core space.

## Idea

As mentioned in the previous unit about the generation process, our wave core space file will consist of multiple sets of wave function parameters. It will be a file similar to JSON/NPZ. Then, "Calculate wave function field and probability cloud in 3D space" is essentially a process of getting the WSF file.

- **Generate parameters needed for the wave function** (Wave vector components $k_x$, $k_y$, $k_z$; Angular frequency $\omega$; Amplitude $A$; Center position $\text{Center}_x$, $\text{Center}_y$, $\text{Center}_z$; Velocity components $v_x$, $v_y$, $v_z$; Base decay rate $d_0$; Axis scaling factors $\mathbf{S}$; Spherical harmonic weights $w_{l,m}$; Information system values for controllable domains; Constant offset term C)
<br>
↓
<br>
- **Calculate wave function field and probability cloud in 3D space** (world parameters: we need space (x, y, z) and time (t) parameters to compute the solution of the equation)
<br>
↓
<br>
...

Then as mentioned in blog "00 Discuss Real World Models", our model is bidirectional, and our main components can pass information to each other, the model can be used for world generation and understanding.

Therefore, if we can reverse-engineer an image or video back into wave space, we can accomplish tasks such as image or video generation based on reference images or 4D reconstruction. Moreover, our reference images can attempt to use only conditional input images like ControlNet, because our model has inherently learned conditions such as pose, depth, etc., and we have also learned information about materials, characters, lighting, and so on.

Using images to reconstruct wave space is quite simple - we just need to operate the pixel layer in reverse. However, for conditional generation, the problem we need to solve is how to collapse the wave to conform to conditions (that is, in the case where some channels among the 256 channels are determined, complete the remaining channels, and even complete more extensive the rest of the generated image) into pixel images.

## How to control the core space

### Implement Controllable Generation with Fixed Partial Results

Our choosed method is: Reverse-engineer the results, then forward reason, relying on the inherent properties of flow models to operate in high-dimensional space to achieve similar effects.

We're considering encoding as many domains as possible—such as materials, physics, etc.—as controllable domains into the wave. This information can all be reflected in the solution of the wave function; when reconstructing the wave space from multiple perspectives of the wave, we only need to separate certain spectra (On May 6th, 2025, I accomplished this function by encoding the information into waves).

Pose and lighting are still uncertainties. 1. It seems that in the process of restoring real images to wave space, the shape of the wave can achieve similar pose control functionality. As in the previous question, ControlWave controls controllable generation not through ControlNet training, but through information recorded in wave space, just as we need OpenPose pose JSON files rather than pose visualization images. We need to build in some such preprocessing/extraction models. 2. Lighting information needs to work with different angles, which requires further consideration on how to create engine-like light sources.

## Basic Generation (Control like PS and Rendering like UE/Blender)

### Implement Real-time Pixel-Level Preview

For real-time output during preview, we can first generate RGB and then generate other channels, but this must ensure consistency between preview and exported images. Our choosed method is: Separate generation modes: Split into ordinary three-channel generation and full generation (during export) modes. (Preview and export results may not be consistent, need to ensure a good technique)

For real-time output during preview, we implement a dual-mode generation system that balances speed and quality. Our approach enables fast previewing while ensuring consistency with the final exported results. We separate generation into two modes:

- **Preview Mode:** Generates only RGB channels (3 channels) for quick visualization
- **Export Mode:** Generates all channels (256 channels) for the complete wave field

To ensure consistency between preview and export results, we implement a random seed recording mechanism. When a user initiates a preview, the system:

1. Records the exact random seed used for the UNet velocity field generation
2. Generates a 3-channel velocity field for quick ODE decoding and display
3. When the user chooses to export, the system reuses the identical random seed to generate the full 256-channel velocity field
4. The exported result's RGB channels match precisely with the preview image

This technique guarantees that what users see in preview is exactly what they'll get in the export, just with more additional channels.



### Multi-layer output and semantic area control



### How to use image input for world reconstruction



## Dissuasion

### How to control the pixel network

Manifolds represent low-dimensional structures in high-dimensional space, capable of smoothly and continuously describing the state space of complex systems. They can also be understood as distributions in high-dimensional space, and most generative models today are learning to transform one distribution into another. In this context, we can imagine a scenario where using prompts to generate images is like searching within this space, while visually creating a core space is finding ways to make this space explicitly visible and manipulable.

We can imagine that we think the Earth is flat because it's too large, and we think the scenes we see are two-dimensional planes because they exist on the surface of an immensely vast latent high-dimensional space. We search this manifold through viewpoints and prompts by moving along its surface. Therefore, videos with continuously changing camera positions are our best training data, as they can depict a complete world.

The key to controlling the pixel layer is the reverse process.
