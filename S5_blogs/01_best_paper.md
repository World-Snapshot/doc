# Rethink Best Papers

*“The edifice of Computer Vision has been completed, with only two black clouds remaining - ‘quadratic growth’ and ‘logical physical consistency’. Future generations will only need to increase data and computing power.” -- This is what the big companies say.*

The Best Papers also have their hierarchies, and let's just talk about the interesting ones.

## ResNet and WSG

ResNet emerged to address the problem of gradient vanishing or explosion when model layers increase. In traditional neural networks, each layer extracts features from the previous layer, and as the number of layers increases, problems like degradation usually occur. ResNet avoids these issues by adopting skip connections.

<strong style="color: #666666">If ResNet solves the problem of training depth, then WSG solves the problem of training breadth.</strong> In a certain Greek mythology novel, there is such a plot:

"The celestial bodies above the ground have physical forms, while those below the ground do not. Therefore, the sun and moon with physical forms exist above the earth, while the formless sun and moon exist in the underworld.

The sun symbolizes the yang force, so the sun in the sky is stronger than the sun in the underworld; the moon symbolizes the yin force, so the moon in the underworld is stronger than the moon in the sky.

The physical sun was born first, so all concepts of [sun] originate from it; the formless moon was born first, so all concepts of [moon] stem from it. The above and below correspond to each other, and this is your achievement as the divine king."

This plot has a strong style of transformation between reality and virtuality. After completing the conception of WSG (World Snapshot Graphics), I thought, if training depth relies on models, should training breadth still rely on models/algorithms?

Humans have 5 senses, and if we add more, would it affect how we perceive the world? Some animals don't have hearing, while others don't have vision - does this affect how they perceive the world? The answer is no. Being able to distinguish a few more types of light wouldn't make much difference for humans. Bats can understand the world through sound waves; it's just a different direction of evolution.

Therefore, the answer might be just the opposite - training breadth should be achieved through upgrading data formats - in the AI world, perhaps the moon is in the underworld. We should construct new data structures to enable models to perceive the world anew correctly.

## Diffusion, ControlNet and WaveGen

In the past 5 years, LLM has been one of the most brilliant achievements in NLP, while generative models have been one of the most brilliant achievements in CV.

However, CV's images cannot be fully controlled yet, and videos can hardly generate coherent movies longer than 2 hours. Compared to LLM, it seems somewhat weak. As for the reasons, I've already mentioned them in the Song of Computer Vision (2024), so I won't elaborate further.

I believe the CV field should be completely unified: standardization of basic formats; unification of generation methods across dimensions, like 2D (image/video), 3D (scene), and 4D (dynamic scene). There should be not only explicit control methods like ControlNet but also implicit constraint control methods through theory. Thus, WaveGen was born.

Just as GPT destroyed dozens of NLP downstream tasks, <strong style="color: #666666">WSG at the fundamental level has made almost all modality fusion methods obsolete, WaveGen will make many previous methods (GAN, Diffusion, Point Cloud, NeRF, 3DGS etc.) become mundane.</strong>

However, as generation models that made great contributions before, they still have potential in the future WSG era, or more precisely, any generation model will shine through WSG.

**Note1:** On April 9, 2025, I suddenly realized that ControlNet is based on several parameter-based controls, while we implement dozens of conditional controls through different WSG channels. RGB colors themselves are actually 3 types of conditional controls (3 color lights), and an image itself is the result of being controlled by these 3 types of light. This means that ControlNet's parameter-based conditional control and our data structure-based conditional control are essentially the same, except that we have separated it out. As Blog 07 mentioned, conditions are hidden within the model. Using more code blocks for conditional control is actually the same as controlling in parallel through channels. This is also why IC-Light is able to work.

## Point Cloud, NeRF, 3DGS, and WSF

Existing point cloud and Gaussian models are in some sense prototypes of WSG, except they didn't combine it with probability or the image itself, which makes it a bit cumbersome. In the future, point cloud and Gaussian-related technologies can be integrated into WS-related model methods. This is very promising.

NeRF is somewhat like WSF under pure probability, though NeRF cannot transform to explicit representation. However, compared to point clouds, it can reduce the occurrence of holes. Overall, previous 3D methods were all quite good, though they each seem to have their own drawbacks, but as time passes, many people try to compensate for these through various methods.

It would be better if WSG could use LiDAR to fill its absolute distance channel, rather than relying on predicted distances. If it's necessary to use predicted distances, I prefer using metric distances or affine-invariant distances, as this makes reconstruction and rendering faster. Although humans perceive the external world through relative feeling, everything in nature ultimately has its natural scale.

## The real challenges in the field of computer vision at present

Currently, there are many genuine problems in the field of computer vision that need to be addressed. However, due to their complexity, these problems have been overlooked by researchers over time. They have transformed the difficult issues encountered in expanding the knowledge frontier into something that seems worthy of solving, but in reality, the real problems remain here.

We must not forget what the real problems are. We cannot walk with our eyes blindfolded. This is an expenditure of financial resources, human efforts and the youth's enthusiasm. Now let's set out towards the real problems.

*Conceived this blog on 23th Dec 2024 and completed on 23th Dec 24, Updated on 9th Apr 2025*