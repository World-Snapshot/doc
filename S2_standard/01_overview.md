# Overview

You must be curious: After reading that song, we felt the guidance and truth. But how should we proceed? There are multimodal papers being produced every moment, aren't there?

The answer is [Computer Vision](https://en.wikipedia.org/wiki/Computer_vision) - the name of the song.

Computer Vision is a science that uses cameras and computers to replace human eyes for recognition, tracking and measurement of targets, and further processes information with computers to create images more suitable for human eye observation or transmission to instrumental detection.

The way humans recognize the world is through vision, and the common basic unit is pixels. [Pixels](https://en.wikipedia.org/wiki/Pixel) are the basic unit of image display, indivisible, determined by the color values of three lights.

However, pixels are the basic unit of image display, not the basic unit of our cognitive world! If we want to store the entire world in computer graphics, i.e., world snapshot graphics, we should change the basic unit.

## Definition

I make the following definitions:

- **World Pixels**, world elements, world points, also called world snapshot atoms, are basic units that add more attribute values to pixels, not just color values. World pixels have more than 3 channels to record more information about a scene.

- **World Snapshot Graphics**, abbreviated as .wsg format, also called world snapshot or world video frame, is a new graphic format composed of world pixels, with each world pixel point in its proper position in the image, but containing more information.

- **World Snapshot Video**, abbreviated as .wsv format, is a continuous world piece composed of several world snapshots.

- **World Snapshot Model**, abbreviated as WSM, is a generative model that learns transformations among World Snapshot variables. WSM v1 treats RGB, geometry, motion, pose, material, physical properties, semantics, and sparse structures as endpoints in one directed visual-task graph.

## Explain

When a model reads graphics, it will read a pixel as a basic tensor with 3 values. In WSG version 1, each world pixel is a basic tensor with 256 values.

Since there aren't many models that directly process the color values of each pixel, and won't notice, damage, or adjust these basic units, most models should be able to train world snapshot graphics with minimal modifications. At most, the most basic tensor flow between the entire input and output needs to be adjusted.

We provide the active WSG and WSV standards in the next sections, together with the injectors, extractors, readers, and visualization tools in the [WSG repository](https://github.com/World-Snapshot/wsg). The earlier World Snapshot Fields proposal remains available in the V0 documentation archive as part of the project's design history, but it is not part of the current WSM v1 implementation.

## Supplement

I found theoretical support on March 21, 2025: In a highly-cited physics paper titled ["The Large-N Limit of Superconformal Field Theories and Supergravity"](https://link.springer.com/content/pdf/10.1023/A:1026654312961.pdf), it mentions that a (d+1)-dimensional gravity theory (such as supergravity in anti-de Sitter space AdS) can be completely described by a d-dimensional conformal field theory (CFT). More simply generalized: an (n+1)-dimensional space under appropriate conditions can be represented by an n-dimensional space.

This is similar to a hologram, where three-dimensional images can actually be reproduced through a two-dimensional surface. AdS/CFT elevates this concept to the level of physical theory, providing a concrete implementation of the Holographic Principle, which suggests that <strong style="color: #666666">all physical phenomena occurring in three-dimensional space (such as gravity, particle motion, etc.) can be "encoded" in field theory on a two-dimensional boundary.</strong> That is, information about a system can be encoded on its boundary, and this is a method supported by physical theory to create a model of the ideal world.

**Note1:** On August 17th, 2025, I realized that my job was actually about realizing the physical [holographic theory](https://en.wikipedia.org/wiki/Holographic_principle). This physical theory posits that the properties of a space (such as physical information) can be encoded onto its boundaries, just as a world can be captured by the event horizon of a black hole. The history of the "physical holographic theory" or the "cosmic holographic theory" is quite long and has been highly regarded by many Nobel Prize-winning physicists. I essentially rediscovered, proposed, and implemented this idea in the field of computer vision.

*Please read blogs "00 Discuss Real World Models"*