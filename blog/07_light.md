# Tensors are Basis of Light

## Introduction

Photons are the smallest unit of real light. Does light in virtual world have units? If so, what is the unit of light? If we want to thoroughly train the entire world, we should carefully consider this question.

## Camera as a Real World Sampler

For one square meter of the real world, calculating with Planck scale (about 10^-35 meters) as the smallest unit, 1 square meter = (10^35)^2 = 10^70 basic "pixel" units. However, at the quantum scale, photon-matter interactions are more like energy exchanges rather than traditional reflection.

In conventional optics, diffraction limits determine the smallest focal point. According to Rayleigh criterion, minimum focal diameter ≈ 1.22λ/NA. With visible light (λ≈500nm) and high NA(≈0.95), minimum focal point ≈ 640nm ≈ 6.4×10^-7 meters. Therefore, theoretical pixels per square meter: (1/6.4×10^-7)^2 ≈ 2.44×10^12 pixels. This is more practical than the Planck scale calculation, representing classical optics' actual limit.

This number is astounding - a square meter image is roughly the same parameter size as a 200B large language model. And cameras were invented nearly 200 years ago. We can say each photo greatly reduces redundant information, sampled by cameras for humans and AI models.
Therefore, I can say original RGB images are already a type of world representation. (My thought: perhaps "vision tokens" aren't very important)

## Optical Tracking Is Not Important

After developing and defining "world pixels," we can consider the importance of accompanying optical properties.
First, I believe previous images couldn't control lighting because: 1. lack of good text annotations - input text didn't correlate with image lighting; 2. without object IDs, models confuse rocks with animals - material labels should exist, at least with implicit vector differentiation (eg, water has a material attribute of 0.78 and wood has a material attribute of 0.44). Current image generation models rely entirely on learn natural world distribution, which is too cumbersome.

For example, Lvmin Zhang's [IC-Light](https://github.com/lllyasviel/IC-Light) specifically studied optics, making image lighting noticeable to models, and it also get the correct normals. Some models train on RGBA, enabling image and transparency generation between models. These are directions we researchers should note.

Their similar work proves: 

Tensors can effectively capture essential visual features without detailed light transport calculations. Modern AI models demonstrate impressive visual generation even with simplified lighting models, AI can learn appropriate light distribution, suggesting full optical simulation may be unnecessary overhead.

 We can add appropriate optical properties to RGB three-channel tensor flows with paths to replace graphics components, implementing much more concise AI-based optical simulation.

So, for virtual worlds and world snapshot models, I can say: tensors are the foundation of light.

*Conceived this blog on 22th Jan 2025, Completed on 23th Jan 2025*