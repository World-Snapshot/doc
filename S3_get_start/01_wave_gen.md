# Learn Quantum Wave Function Generation (WaveGen)

*"God plays dice, our world snapshot does play dice too."*

## Overview

World Snapshot aims to unify digital reality at the pixel level, and [WaveGen](https://github.com/World-Snapshot/WaveGen) is its sharpest weapon. We defined and discussed the forms of WSG, WSV, and WSF in sequence, but I never said we would train these three formats separately.

In theory, WaveGen can directly train a continuous world field (WSF). When we fix the angle, it becomes WSV, and when we take a specific frame from it, we get WSG image generation. Therefore, we will try to directly generate a dynamic world scene, which wave collapses according to viewing angles and frame numbers, and then export the format we want.

## Background

## Idea

## Implementation

## Discussion

Our wave function generation method essentially uses multiple sets of wave functions to construct a core space that can simulate the world. This space is inherently physical: it possesses characteristics such as energy, probability, density, mass, temporal evolution, interactive constraints between different parts, different scale perspectives, 1-4D unification, and transformation between virtual and real states (both explicit and implicit).

This core ("world core" or "heart of the world") can be viewed as world tokens space, where each wave function is a world token. For example, when we generate Batman and Superman fighting from text, the process or results of generation might be different each time. However, after training, these superimposed and entangled abstract world representations that evolve with time in the core space will always strive to be as reasonable as possible.

In my WaveGen, the focus is more on using text to control this "world core" or "heart of the world" to utilize its generative capabilities. In the future, people could develop something like ControlWave to try controlling this "world core" through other methods. Currently, the reconstruction capability might be relatively weak and needs exploration.

WaveGen's "world core" is an expandable superposition of complex waves that can simulate the world, with extremely free and expandable expressiveness. It's almost like a genius creation. Its characteristics are difficult to summarize:

Compared to diffusion, its virtual-real transformation and noise addition/removal are similar, and it inherently acts like a single-step diffusion model - equivalent to diffusion with fewer layers. Since wave functions only need very simple parameters to simulate a world, it saves considerable cross-attention space. Its information about world distribution is mainly stored in the pixel space decoding process.

Compared to point clouds, they are like a form of our foundation, but they're difficult to compare. The difference might be that we have more information and a "heart of the world" to unify the underlying logic of the world in an abstract way.

Compared to NeRF, it's equivalent to using hundreds of wave functions instead of Gaussians for reconstruction. Our functions are virtual and need decoding. This is like software engineering decoupling rule. We use pixels to render the world, which makes editing and processing convenient and saves enormous space. Although we also need to sample points, we're much faster than MLP. The disadvantage is that we're too free because we're essentially like Text2NeRF or Text-to-4DGS, a generative model. For world reconstruction or reconstruction using reference images, we could consider recovering wave characteristics from reference images to guide generation, or increase the number of wave function groups while reducing pixel freedom.

Compared to 3DGS, we're equivalent to using probability clouds instead of Gaussian kernels, and they're fundamentally quite similar. If we use 99% wave functions and 1% pixel decoding, we might be like isomers.

## Prospect

At the WSG level, I hope we can generate a perfect photo of a world scene. At the WSV level, we can generate an entire movie at once, or even generate continuous video spanning several days. At the WSF level, we hope to create a naturally coherent world where every user is a creator god.

I hope AI can generate a happy world without fatigue, without regret, only happiness and dreams coming true. When users enter it, they can even live a happy life forever. I mean: <strong style="color: #666666">Hope humans will have the ability to create the subordinate universe from now.</strong>

*Please read blogs 07*