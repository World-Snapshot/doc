# World Snapshot Video (WSV) Format Specification
Version: 1.0;
Last Updated: 2025-10-02;
History Version at <a href="https://github.com/World-Snapshot/doc/commits/main/" target="_blank">link</a>

## Overview
WSV (World Snapshot Video) is a collection of multi-frame WSG files, representing a single-perspective dynamic visualization scene/video file. For WSV files, the key challenge lies in how to process audio information that spans across time.

## Idea

Under WSG v1, we bind the sound of each frame with the object mask areas (containing IDs for objects, people, and regions) in that frame. Each segmented area has a sound source ID.

When we play certain segments in the generated video that contain these segmented areas, the sound source ID naturally appears, and the generated segment naturally carries sound.

Then, I want random damage to any pixels in this area not to affect the overall sound: specifically, during reading, it's not necessary to read all pixels - only partial pixel reading is required. After reading enough pixels, it will automatically discover that sufficient sound information has been obtained.

For example, when a WSV video player starts reading pixels randomly, there will be a progress bar. When the progress bar reaches 100%, it indicates that you have obtained the complete sound of the sound-emitting object in this frame. Perhaps only a few hundred pixels out of tens of thousands of pixels are needed to obtain the sound. In this way, random destruction of any pixels will not damage the sound.

## Method

I use redundant distributed storage algorithms to handle this.

For audio with sound sources, audio data is distributed throughout the entire instance mask region using cyclic redundant storage (typically the largest instance, as the original dataset only has textual semantic annotations):

1. Data Compression and Encoding:
   - Audio preprocessing: Downsample original audio (typically 44.1kHz stereo) to 8kHz mono, reducing data rate from approximately 164KB/s to 8KB/s. Then quantize floating-point audio samples to 8-bit signed integers (-128 to 127), achieving a 20x compression ratio.
   - Each second of audio requires 8000 bytes of storage space
   - Data structure: 12-byte header (4-byte magic number + 2-byte instance ID + 2-byte length + 4-byte checksum) + audio data

2. Structured Data Encapsulation: Create a 14-byte header containing:
   - Magic number (4 bytes): [0xF0, 0x0F, 0xF0, 0x0F], used for data integrity verification
   - Frame index (2 bytes): Identifies which frame's audio this is
   - Data length (4 bytes): Number of bytes in audio data (typically 8000)
   - Checksum (4 bytes): Cumulative sum of audio data, used for verification

3. Redundant Distributed Storage:
   - Audio data is cyclically stored across all valid pixels within the mask region
   - Each pixel utilizes 10 audio channels (175-184) to store 10 bytes of data
   - For 8012 bytes of complete data (header + 1 second audio), only 753 pixels are needed to store one complete copy, creating an audio pattern that facilitates CNN learning. A typical mask generally has 3k regions.
   - If the mask region has 10000 pixels, approximately 10 complete copies can be stored, achieving 10x redundancy. The AVIS dataset has an average mask area of 9055.

4. Fault-Tolerant Reading Mechanism:
   - Reading starts from any pixel in the mask region and proceeds sequentially
   - Magic numbers identify data start positions
   - Only 753 consecutive valid pixels are needed to recover complete audio
   - Even if 90% of pixels are corrupted, audio can still be recovered as long as 753 consecutive pixels remain intact

5. Float16 Precision Adaptation:
   - Uses stable value mapping formula: (byte_val / 255.0 - 0.5) * 100, mapping to [-50, 50] range
   - Intelligently detects and corrects data errors caused by float16 precision loss
   - For example: length field 8000(0x1F40) might be read as 7743(0x1E3F), and the system automatically corrects this

For scene audio, which has no mask, or descriptive text for the entire image will be converted to audio and stored in channels 185-184 of the entire image.

## Summary

Sound is the intersection of NLP and CV. Sound is a specific object, and sound is a visual pattern.


*Please read blogs "03 Time Flowing in Graphics" and "04 Create Laplace Demon"*