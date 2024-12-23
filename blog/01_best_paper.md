## Rethink Best Papers

The Best Papers also have their hierarchies, and let's just talk about the interesting ones.

### ResNet and WSG

ResNet emerged to address the problem of gradient vanishing or explosion when model layers increase. In traditional neural networks, each layer extracts features from the previous layer, and as the number of layers increases, problems like degradation usually occur. ResNet avoids these issues by adopting skip connections.

If ResNet solves the problem of training depth, then WSG solves the problem of training breadth. In a certain Greek mythology novel, there is such a plot:

<p>The celestial bodies above the ground have physical forms, while those below the ground do not. Therefore, the sun and moon with physical forms exist above the earth, while the formless sun and moon exist in the underworld.</p>

<p>The sun symbolizes the yang force, so the sun above is stronger than the sun in the underworld; the moon symbolizes the yin force, so the moon in the underworld is stronger than the moon above.</p>

<p>The physical sun was born first, so all concepts of [sun] originate from it; the formless moon was born first, so all concepts of [moon] stem from it. The above and below correspond to each other, and this is your achievement as the divine king.</p>

This plot has a strong style of transformation between reality and virtuality. After completing the conception of WSG (World Snapshot Graphics), I thought, if training depth relies on models, should training breadth still rely on models/algorithms?

Humans have 5 senses, and if we add more, would it affect how we perceive the world? Some animals don't have hearing, while others don't have vision - does this affect how they perceive the world? The answer is no. Being able to distinguish a few more types of light wouldn't make much difference for humans. Bats can understand the world through sound waves; it's just a different direction of evolution.

Therefore, I'm probably doing the right thing - in the AI world, perhaps the moon is underground. We should construct new data structures to enable models to perceive the world anew.

### Diffusion Models, ControlNet, Gaussian & WSG

In the past 5 years, LLM has been one of the most brilliant achievements in NLP, while generative models have been one of the most brilliant achievements in CV.

However, CV's images cannot be fully controlled yet, and videos can hardly generate coherent movies longer than 2 hours. Compared to LLM, it seems somewhat weak. As for the reasons, I've already mentioned them in the Song of Computer Vision (2025), so I won't elaborate further.

What I want to discuss is that diffusion models, as an elegant generative model, still have potential in the future WSG era, or rather, any generative model will shine through WSG.

The existing Gaussian model is in some sense a prototype of WSG, except that they haven't combined it with the images themselves, making it a bit cumbersome. In the future, Gaussian-related technologies can be integrated into WS-related model methods. This is very promising.

It would be better if WSG could use LiDAR to fill its absolute distance channel, rather than relying on 3DGS-predicted distances. I probably won't consider filling Gaussian properties into WSG channels for now.

*Conceived this blog on 23 Dec 24 and completed on 24 Dec 24*