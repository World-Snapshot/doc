# Tensors are Basis of Light

## Introduction

Photons are the smallest unit of real light. Does light in virtual world have units? If so, what is the unit of light? If we want to thoroughly train the entire world, we should carefully consider this question.

## Camera as a Real World Sampler

For one square meter of the real world, calculating with Planck scale (about 10^-35 meters) as the smallest unit, 1 square meter = (10^35)^2 = 10^70 basic "pixel" units. However, at the quantum scale, photon-matter interactions are more like energy exchanges rather than traditional reflection.

In conventional optics, diffraction limits determine the smallest focal point. According to [Rayleigh criterion](https://en.wikipedia.org/wiki/Angular_resolution#The_Rayleigh_criterion), minimum focal diameter ≈ 1.22λ/NA. With visible light (λ≈500nm) and high NA(≈0.95), minimum focal point ≈ 640nm ≈ 6.4×10^-7 meters. Therefore, theoretical pixels per square meter: (1/6.4×10^-7)^2 ≈ 2.44×10^12 pixels. This is more practical than the Planck scale calculation, representing classical optics' actual limit.

This number is astounding - a square meter image is roughly the same parameter size as a 200B large language model. And cameras were invented nearly 200 years ago. We can say each photo greatly reduces redundant information, sampled by cameras for humans and AI models. Therefore, I can say original RGB images are already a type of world representation. (My have an additional thought: perhaps "vision tokens" aren't very important)

Therefore, I believe when computational power is sufficient, there's no need to use VAE to reduce the dimensionality of real images, although this might be why some image generation models are so smooth. At least WaveGen shouldn't need it much - even every pixel in the distance is valuable data, like a fish pond where we should try to reach the muddy bottom.

However, the pixel decoding layer can also use some compression techniques, because this does not affect the upper limit of the model, we can adjust the compression rate at any time, or change the generation method.

**Note:** On June 14, 2025, I originally intended to not use VAE at all because its randomness would ruin the accuracy of our bidirectional reasoning (it cause that we couldn't achieve 100% accuracy on all estimation tasks. If we abandon the VAE, the RF + Unet structure can enable our world snapshot model to achieve an accuracy rate of nearly 100% on thousands of tasks. Once I have 10,000 GPUs available, I will give it a try), but without using VAE, it would be almost impossible to train. I had to give in temporarily.

## Optical Tracking Is Not Important

After developing and defining "world pixels", we can consider the importance of accompanying optical properties.
First, I believe previous images couldn't control lighting because: 1. lack of good text annotations - input text didn't correlate with image lighting; 2. without object IDs, models confuse rocks with animals - material labels should exist, at least with implicit vector differentiation (eg, water has a material attribute of 0.78 and wood has a material attribute of 0.44). Current image generation models rely entirely on learn natural world distribution, which is too cumbersome.

For example, Lvmin Zhang's [IC-Light](https://github.com/lllyasviel/IC-Light) specifically studied optics, making image lighting attribute noticeable to models, and it even also get the correct normals in different lighting environment. Some models train on RGBA, enabling image and transparency generation between models. These are directions we researchers should note.

Their similar work proves:

Tensors can effectively capture essential visual features without detailed light transport calculations. Modern AI models demonstrate impressive visual generation even with simplified lighting models, AI can learn appropriate light distribution, suggesting full optical simulation may be unnecessary overhead.

We can add appropriate optical properties to RGB three-channel tensor flows with paths to replace graphics-based Optical Tracking components, implementing much more concise AI-based optical simulation. Previous work didn't try this thoroughly, and they didn't actually use AI to build fully optical tracking. True AI optical tracking starts here.

## The Human Eye is an Optical Interpreter

What is the color of objects, and what is the essence of color? Color is the perception of electromagnetic waves of different wavelengths on human cone cells. For example, green light is just electromagnetic waves with wavelengths between 492-577 nanometers, and other species may perceive it differently.

In the past, training world information was conducted through images composed of three primary colors. The main reason for previously using RGB three channels to a large extent was that this is a format that can be easily read by human eyes, meaning that human eyes are a limited optical interpreter.

Computer vision based entirely on RGB and other few channels is, in a sense, very limited learning, as we have ignored too much valuable information. This is also why 3D vision is becoming increasingly popular. WavGen may also have valuable information that hasn't been noticed, but it provides a convenient platform, a new perspective.

Perhaps it's the newly supported potential and kinetic energy calculations, which can support pixel-level momentum conservation, or perhaps it's the naturally convenient multi-modal fusion, or formula-level time support, or virtual-real interaction calculations, or perhaps it's highlighting the value of AI optics...

So, for virtual worlds and world snapshot models, I can say: tensors are the foundation of light.

*Conceived this blog on 22th Jan 2025, Completed on 23th Jan 2025, Updated on 7th Feb 2025*