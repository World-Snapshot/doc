# ControlWave

## Overview

ControlWave is a WebUI that makes WaveGen more convenient to control. Unlike [ControlNet](https://github.com/lllyasviel/ControlNet?tab=readme-ov-file), WaveGen natively supports various controls and doesn't require training additional neural blocks like ControlNet does. Therefore, this is just a WebUI.

ControlWave is mainly divided into two parts, one concerning the core space and one concerning the pixel layer. It's like an inner world and an outer world. For ControlWave, first it should have all the basic functions of ControlNet, and then by controlling the core space, it have more amazing capabilities.

## Idea

As mentioned in the previous unit about the generation process, our WSF file will consist of multiple sets of wave function parameters. It will be a file similar to JSON. Then, "Calculate wave function field and probability cloud in 3D space" is essentially a process of loading the WSF file.

- **Generate parameters needed for the wave function** (Wave vector components $k_x$, $k_y$, $k_z$; Angular frequency $\omega$; Amplitude $A$; Center position $\text{Center}_x$, $\text{Center}_y$, $\text{Center}_z$; Velocity components $v_x$, $v_y$, $v_z$; Base decay rate $d_0$; Axis scaling factors $\mathbf{S}$; Spherical harmonic weights $w_{l,m}$)
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

## Basic Generation (Rendering)

## How to use image input for world reconstruction

## How to control the core space

## How to control the pixel network
