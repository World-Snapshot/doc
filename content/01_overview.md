# Overview

You must be curious: After reading that song, we felt the guidance and truth. But how should we proceed? There are multimodal papers being produced every moment, aren't there?

The answer is Computer Vision - the name of the song.

Computer Vision is a science that uses cameras and computers to replace human eyes for recognition, tracking and measurement of targets, and further processes information with computers to create images more suitable for human eye observation or transmission to instrumental detection.

The way humans recognize the world is through vision, and the common basic unit is pixels. Pixels are the basic unit of image display, indivisible, determined by the color values of three lights.

However, pixels are the basic unit of image display, not the basic unit of our cognitive world! If we want to store the entire world in computer graphics, i.e., world snapshot graphics, we should change the basic unit.

## Definition

I make the following definitions:

- **World Pixels**, world elements, also called world points, are basic units that add more attribute values to pixels, not just color values. World pixels have more than 3 channels to record more information about a scene.

- **World Snapshot Graphics**, abbreviated as .wsg format, also called world snapshot or world frame, is a new graphic format composed of world pixels, with each world pixel point in its proper position in the image, but containing more information.

- **World Snapshot Video**, abbreviated as .wsv format, is a continuous world segment composed of several world snapshots.

## Explain

When a model reads graphics, it will read a pixel as a basic tensor with 3 values. In WSG version 1, each world pixel is a basic tensor with 256 values.

Since there aren't many models that directly process the color values of each pixel, and won't notice, damage, or adjust these basic units, most models should be able to train world snapshot graphics with minimal modifications. At most, the most basic tensor flow between the entire input and output needs to be adjusted.

We provide specific standards for WSG and WSV in next section. We also provide img2wsg converter, wsg reader, wsg interpreter, and wsv player.