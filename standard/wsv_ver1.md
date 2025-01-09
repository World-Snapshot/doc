# World Snapshot Video (WSV) Format Specification
Version: 1.0
Last Updated: 2025-1-9

## Overview
WSV (World Snapshot Video) is a collection of multi-frame WSG files, representing a single-perspective dynamic visualization scene/video file. For WSV files, the key challenge lies in how to process audio information that spans across time.

## Method

Under WSG v1, we bind the sound of each frame with the object mask areas (containing IDs for objects, people, and regions) in that frame. Each segmented area has a sound source ID.

When we play certain segments in the generated video that contain these segmented areas, the sound source ID naturally appears, and the generated segment naturally carries sound.

Then, I want random damage to any pixels in this area not to affect the overall sound: specifically, during reading, it's not necessary to read all pixels - only partial pixel reading is required. After reading enough pixels, it will automatically discover that sufficient sound information has been obtained.

For example, when a WSV video player starts reading pixels randomly, there will be a progress bar. When the progress bar reaches 100%, it indicates that you have obtained the complete sound of the sound-emitting object in this frame. Perhaps only a few hundred pixels out of tens of thousands of pixels are needed to obtain the sound. In this way, random destruction of any pixels will not damage the sound.

I use redundant distributed storage algorithms to handle this.

*Please read blogs 03 and 04*