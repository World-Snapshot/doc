# World Snapshot Field (WSF) Format Specification
Version: 1.0
Last Updated: 2025-01-09

## Overview

WSF (World Snapshot Fields) is a hybrid neural radiance field file synthesized from two or more angles of wsg/wsv files through 3D reconstruction methods. For WSF files, the key challenge lies in handling the massive number of pixels.

## Background

NeRF is an implicit representation where each point in space has a color and probability, without concept particles. It's not easily editable.

3DGS is an explicit representation where each point in space is a Gaussian body, which overlap to produce transparency and color. It's easy to edit and renders quickly, but Gaussian bodies are not easily compatible with existing tools.

Our WSF is a hybrid neural radiance field that can serve as both an explicit and implicit representation.

## Idea

Although our WSG pixels themselves contain abundant information that helps us train the entire world more realistically, this creates an enormous computational load. (Point clouds have this disadvantage too)

Therefore, when training, we set up a 3x3 pixel grid in the WSG image, where the center pixel is real and the surrounding 8 pixels are virtual. Virtual pixels are represented through quantum probability states, allowing us to reduce computation by 1/9 while maintaining quality. We can also expand the grid, as long as the side length remains odd.

Through this approach, WSF has concept particles like 3DGS while maintaining differentiable, calculable functions like NeRF, reducing computational load. It possesses advantages of both systems. Additionally, each of our concept particles has its own color, requiring no additional rendering.

How should we train this kind of data that combines virtual and real, particles and probability? Facing this familiar scenario, I thought of the quantum wave function:

## Quantum Wave Function

In quantum physics, a [wave function](https://en.wikipedia.org/wiki/Wave_function) (or wavefunction) is a mathematical description of the quantum state of an isolated quantum system. In one common form, it indicates that the square of the modulus of a position-dependent wave function is the probability density of measuring a particle at a given position. The integral of the square of the wave function's modulus over all degrees of freedom of the system must equal 1, a condition called normalization. Since the wave function is complex-valued, only its relative phase and relative magnitude can be measured; its value alone cannot tell us the magnitude or direction of measurable observables. One must apply quantum operators (whose eigenvalues correspond to possible sets of measurement results) to the wave function ψ and calculate the statistical distributions of measurable quantities.

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
<summary>Main Application Scenarios:</summary>

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

<details>
<summary>Potential Challenges:</summary>

* Numerical stability of wave function evolution
* Precise control of boundary conditions
* Mapping text features to wave function parameters
* Optimization of computational efficiency
</details>

If we can ensure that quantum mechanical probability distribution calculations (i.e., predictions of superposition probability of pixel states) are faster than 3DGS's Gaussian calculations, we will be faster than 3DGS.

## Method

**Note 1:** Existing quantum GANs, quantum diffusion models, and quantum generative models all use existing generative models to explore applications in the quantum domain. Some attempt to generate complex mazes or structures, unrelated to image and scene generation. Others involve "wavelet diffusion" and "wavelet transforms" in the frequency domain, which are unrelated to the properties of quantum waves and their collapse. Unlike previous approaches, we are the first work to focus on image generation through quantum wave functions. 

*Please read blogs 01 and 05*