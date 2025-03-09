# World Snapshot Field (WSF) Format Specification
Version: 1.0;
Last Updated: 2025-01-09;
History Version at <a href="https://github.com/World-Snapshot/doc/commits/main/" target="_blank">link</a>

## Overview

WSF (World Snapshot Fields) is a hybrid neural radiance field file could synthesized from two or more angles of wsg/wsv files through 3D reconstruction methods. For WSF files, the key challenge lies in handling the massive number of pixels.

## Background

NeRF is an implicit representation where each point in space has a color and probability, without concept particles. It's not easily editable.

3DGS is an explicit representation where each point in space is a Gaussian body, which overlap to produce transparency and color. It's easy to edit and renders quickly, but Gaussian bodies are not easily compatible with existing tools.

Our WSF is a hybrid neural radiance field that can serve as both an explicit and implicit representation.

## Idea

Although our WSG pixels themselves contain abundant information that helps us train the entire world more realistically, this creates an enormous computational load. (Point clouds have this disadvantage too)

Therefore, when training, I originally intended to set up a 3x3 pixel grid in the WSG image, where the center pixel is real and the surrounding 8 pixels are virtual. Virtual pixels are represented through quantum probability states, allowing us to reduce computation by 1/9 while maintaining quality. We can also expand the grid, as long as the side length remains odd.

Through this approach, WSF has concept particles like 3DGS while maintaining differentiable, calculable functions like NeRF, reducing computational load. It possesses advantages of both systems. Additionally, each of our concept particles has its own color, requiring no additional rendering.

How should we train this kind of data that combines virtual and real, particles and probability? Facing this familiar scenario, I thought of the quantum wave function:

## Quantum Wave Function

In quantum physics, a [wave function](https://en.wikipedia.org/wiki/Wave_function) (or wavefunction) is a mathematical description of the quantum state of an isolated quantum system. In one common form, it indicates that the square of the modulus of a position-dependent wave function is the probability density of measuring a particle at a given position. The integral of the square of the wave function's modulus over all degrees of freedom of the system must equal 1, a condition called normalization. Since the wave function is complex-valued, only its relative phase and relative magnitude can be measured; its value alone cannot tell us the magnitude or direction of measurable observables. One must apply quantum operators (whose eigenvalues correspond to possible sets of measurement results) to the wave function ψ and calculate the statistical distributions of measurable quantities.

The time-dependent Schrödinger wave function in 3D cartesian coordinates can be expressed as:

ψ(x,y,z,t) = A · e<sup>i(k<sub>x</sub>·x + k<sub>y</sub>·y + k<sub>z</sub>·z - ωt)</sup>

- A: Amplitude (encoded from text)
- k<sub>x</sub>, k<sub>y</sub>, k<sub>z</sub>: Wave vector components (encoded from text)
- ω: Angular frequency (encoded from text)
- x, y, z: Spatial coordinates (sampling points)
- t: Time parameter (user-specified)

Our goal is to build WSF based on wave functions, with the key being training relevant parameters to learn the natural distribution of the world. The core challenge lies in how to control this equation. During inference, users will specify the range of xyz (image resolution, or world range) and time range t. These parameters are used during inference, while parameters like A, k, and ω in the formula need to be learned by the model.

We can then utilize this concept of probability, treating a probability cloud as a virtual world entity. When needed, we decode the wave function solutions through a pixel network into a useful 4D world pixel field. Then I realized that representing the world through just one set of wave functions might not be sufficient, even though the solutions in the complex plane are practically infinite:

We can imagine a disturbance (text input) appearing at the bottom of an ocean, causing changes in the middle layer (wave function features), which ultimately reflects on the surface layer (pixel layer). Although a single wave function can have infinite variations, using just one is like trying to represent everything with a basketball. For example, a large basketball represents animals, a small basketball represents plants, and a one-ten-thousandth amplitude deviation represents species variation. This would certainly be somewhat unstable or limited, although high-dimensional latent space might not actually work this way.

Therefore, we can use multiple sets of wave functions to represent the world's manifestation. When multiple sets of wave functions superimpose, they constrain each other through interference, and they naturally have different states determined by time, capable of representing almost anything. <strong style="color: #666666">They are like the heart or core of the world - imagine countless waves entangled together, like a temporal-spatial ocean, an exquisite membrane with infinite information.</strong>

When applied to image generation, it exhibits some excellent properties:

<details>
<summary>Advantages</summary>

1. Natural Characteristics

* No need for hard-coded rules
* No need for complex attention mechanisms
* Let physical laws handle spatial correlations naturally
* Wave functions automatically satisfy boundary conditions
* Natural spatial continuity and coherence

2. Physical Properties

* Natural transitions produced by wave function interference
* Long-range feature propagation through non-locality
* Controllable randomness from quantum measurements
* Self-organizing properties through wave function interference

3. Control Mechanisms

* Potential field control: Natural guidance of generation process through potential fields
* Boundary control: Utilizing wave function's self-adaptive boundary properties
* Local quantum measurements: Achieving controlled local changes

4. Comparison with Diffusion Models Advantages:

* No need for internal Self-Attention mechanisms in images
* Natural handling of spatial continuity
* Physical constraints provide inherent generation rules

5. Unique Mechanisms

* Controllable randomness through quantum measurements
* Soft constraints provided by potential fields
* Natural adaptation to boundary conditions
* Self-organizing characteristics through wave function interference
</details>

<details>
<summary>Magic Control</summary>

1. Image Editing

* Local redrawing: utilizing boundary adaptation
* Seamless stitching: using periodic boundary conditions
* Style fusion: leveraging wave function interference effects

2. Material Generation

* Fabric wrinkles: using local quantum measurements
* Metal reflections: utilizing wave function phase properties
* Natural textures: using wave interference effects

3. Natural Scenes

* Cloud formations: using wave function continuous evolution
* Water ripples: utilizing wave equation properties
* Leaf movements: using local quantum states

4. Portrait Processing

* Hair variations: using local quantum measurements
* Facial expressions: using potential field control
* Skin details: using wave function interference

5. Architectural Design

* Floor plan generation: using boundary condition control
* Texture mapping: using wave function evolution
* Light and shadow effects: using potential field guidance
</details>

This excites me, and I realize that we can completely abandon the 3x3 or 5x5 calculation division, making all world pixels capable of transforming between virtual and real states. Then we should consider how to combine this idea with data:

## Method

Since WSG itself carries depth information, when we also try to view WSF as a field diffused with virtual points or functions, it leads to confusion in our understanding, as both WSG and WSF are 3D files.

Our intention is to view WSG as a two-dimensional representation of a world from a specific viewpoint (like [Dual-vector foil](https://three-body-problem.fandom.com/wiki/Dual-vector_foil) in novel named "Three Body"). The measured depth serves as the initial value for the z-axis in training, and through the learning process, we learn the true z-values in 3D space.

When a particular viewpoint is observed, we collapse the pixel areas along the line of sight, transforming the point cloud from virtual to real (which aligns well with the real-world [observer effect](https://en.wikipedia.org/wiki/Observer_effect_(physics))). At this point, the point cloud's x and y axes can fill the entire viewpoint area, while the z-axis exists at different depths.

When we change viewpoints, we should collapse again because different viewpoints should have different colors and depths. However, the xyz coordinates and most properties of the same points should remain consistent. During reconstruction, we can consider keeping some data unchanged to reduce computational costs.

In essence, WSF should be a mixed virtual-real field that computes in real-time based on the observer effect. WS rendering is similar to explicit point cloud rendering and can use rasterization, which theoretically should be quite fast. For optimization, we can consider reusing points that have already been quantum collapsed.

In this way, we have roughly conceived the formation of WSF.

**Note 1:** Existing quantum GANs, quantum diffusion models, and quantum generative models all use existing generative models to explore applications in the quantum domain. Some attempt to generate complex mazes or structures, unrelated to image and scene generation. Others involve "wavelet diffusion" and "wavelet transforms" in the frequency domain, which are unrelated to the quantum waves and their collapse. Unlike previous approaches, we are the first work to focus on image generation through quantum wave functions. 

*Please read blogs 01, 05 and 06*