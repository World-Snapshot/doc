# Model Design Guideline Memo

Here I write down my design creation thoughts to help readers better understand why I designed the new model this way. It will help future researchers quickly get started with, use, and improve this model.

This Guideline Memo can be considered as our motivation and what we should do. The main text just tell you how to do it.

## Overview

First, I want to train the entire world, with the key being making the data closer to the world's reality. To train the world itself, I created WSG.

Then, I hope to accelerate training efficiency, as training a real world is too resource-intensive (not those fake/non-ideal world models: e.g., video generation models). Therefore, I considered using quantum wave functions - their mathematics is elegant and is nearly capable of truly describing the world, countless physics papers also said it's a complete way of describing the world.

Next, I want to create a model that can unify 1D, 2D, 3D, 4D, and other dimensions, because training a world naturally means training the all dimension, and the new principle inherently allows for it. I'm designing a completely new model from top to bottom, just like Mendel's peas.

The basic WaveGen has no attention mechanism, just like the original diffusion model paper. It consists of a text encoder module that can understand prompt inputs and a Wave generation module. But temporal continuity is important: although the wave equation itself supports time as a parameter, we need to use frame-to-frame parameter learning to make the world field generation more smooth, like vertical and horizontal road. Also, even if the generated local video segments are consistent, we cannot guarantee that the semantics of the entire video are consistent.

So what should I choose for Temporal Attention? I decided to use RWKV, the best existing linear attention RNN model, abandoning Transformer. Just as the symmetric U-Net was incorporated by diffusion models years later, I believe RWKV and WaveGen are a perfect match - they have too many mutually beneficial properties.

For training strategies, we know there are broadly two categories: self-supervised MSE and reinforcement learning. I lean towards using pure reinforcement learning to train this next-generation new model born in 2025, because for prompt inputs, images themselves are inherently uncertain. Just like DeepSeek-R1 in 25 year, letting the model learn by itself might be more liberating, and RNN states are denser, naturally suited for RL. Moreover, RNN is suitable for causal learning, more elegant than NVIDIA's video generation model named Cosmos in 24 year.

I considered using the seq2seq concept (since our images contain pose information, it like leaves have veins, with stronger constraints), but it doesn't seem very compatible with RNN. I'm also considering MSE as my backup/mixed training strategy.

This sets the tone for the entire new model.

## Idea

And then there were some problems that bothered me. The problems that need to be solved include (but are not limited to):

- How to create the core space, what is the basic unit, what should be in it, and how to implement it?
- In Core Space, how should the high-dimensional features of the wave function be utilized, what information do they possess, especially in direct relation to pixel decoders, how should they work together
- How should Core Space accommodate the principle of least action? What is physics in CV? To what extent should we control reality? What shortcomings of existing models should we target?
- What do we use to understand the high-dimensional features/representations of the world, how do we understand high-dimensional features, how do we control high-dimensional features, and to what extent?
- ...

### Why Not Use Grid/Mesh as the Basic Unit of Core Space? & Decay Methods Selection?

Grid/Mesh is suitable for importing into existing software rendering pipelines, but it is not suitable as the simplest expression method: 1. For a basic wave unit, only about a dozen parameters are needed for implementation, while grids require more parameters. 2. Waves are suitable as carriers for various calculations or information; for core space, we hope it is a mathematical incarnation or expression form. 3. Waves can carry some invariants related to pixels, and are suitable for becoming functional execution methods, such as essentially serving as a physics engine. Therefore, grid can only serve as a derived form of wave space. Of course, I look forward to better work to improve the core space, such as perhaps using pure mathematics and abstract topological information to create a complete space.

Regarding decay, the wave function actually comes with a spherical harmonic function, but I removed it. This is because I think we should use a basic wave and then carve out any shape, rather than generating various shaped probability clouds from the beginning. These two methods should be equivalent; I just find it more convenient to handle. In addition, I have also tried using various functions or SDF (Signed Distance Field) methods for decay, but I feel they are not as natural as spherical harmonic functions.

### The significance and development direction of core space

The core space/heart of the world is actually a world representation after training. According to different directions, one can see different scenes, resulting in output similar to a two-dimensional foil. Then we can successfully match and learn between abstract two-dimensional output and images. Therefore, the core space is a dimensionality reducer, performing conversions between two-dimensional and three-dimensional world representations.

Information in a three-dimensional space isn't as abundant as we imagine; to store this information, we only need the surface that envelops this three-dimensional space (just like all information swallowed by a black hole adheres to its surface, called the black hole horizon). In a video where the camera continuously moves, it can be viewed as continuous observation of a three-dimensional space. Our camera is like processing the world as a space on a spherical surface. We use WSG training, which constructs this two-dimensional/three-dimensional world representation through as much information as possible from the three-dimensional space.

As described in one [paper](https://link.springer.com/content/pdf/10.1023/A:1026654312961.pdf) of the most cited in the field of physics, three-dimensional space + one-dimensional time and two-dimensional space + one-dimensional time are completely dual (can be substituted for each other). It mentions that a (d+1)-dimensional gravity theory (such as supergravity in anti-de Sitter space AdS) can be completely described by a d-dimensional conformal field theory (CFT). More simply generalized: an (n+1)-dimensional space under appropriate conditions can be represented by an n-dimensional space.

This is similar to a hologram, where three-dimensional images can actually be reproduced through a two-dimensional surface. AdS/CFT elevates this concept to the level of physical theory, providing a concrete implementation of the Holographic Principle, which suggests that <strong style="color: #666666">all physical phenomena occurring in three-dimensional space (such as gravity, particle motion, etc.) can be "encoded" in field theory on a two-dimensional boundary.</strong> That is, information about a system can be encoded on its boundary, and this is a method supported by physical theory to create a model of the ideal world.

Roughly speaking, our attempt is to construct such a converter through wave space.

### How to decode or render pixels in real time?

For how to implement decoding generation at the pixel level. I have considered using various generative models including VAE, U-Net, pure decoders, RNN-only, etc., but all seem to be slightly lacking. We know that current models have strong characteristics of mutual learning and fusion. For example, the original diffusion model DDPM contains U-Net, Stable Diffusion added VAE latent space, and its generation end also borrowed some ideas from GANs. Flow-based models are now closely connected with Transformers or autoregressive methods, while stable video diffusion uses technology that combines advantages from multiple approaches.

Therefore, for our generative model, we should choose one that is fastest (because we need to "search" multiple times based on changes in perspective), bidirectional (the definition of an ideal world model), and can provide the longest semantic continuous rendering support (this point cannot be guaranteed, as no one has tried it as of March 20, 2025). After research, I plan to use a flow-based model as the foundation, because flow-based model theoretically supports precise bidirectional generation, and it doesn't even process the image too much (i.e. doesn't extract tokens or use potential space for compression). I love this.

### How do we successfully create physics and causality?

In my view, CV physical generation models are already excellent, they're just missing the final mile of the marathon (they don't handle mutation states like explosions well, and they struggle with causality/state problems). Manifolds represent low-dimensional structures in high-dimensional space, capable of smoothly and continuously describing the state space of complex systems. In physical systems, points on the manifold typically exhibit continuous smooth state transitions as parameters change continuously, because most physical systems are well-posed, satisfying physical law constraints such as energy conservation and mass conservation.

However, when a physical system is at a critical state, even small parameter changes can cause dramatic changes in system state, a phenomenon called mutation. When mutations occur, the system state exhibits discontinuous jumps on the data manifold, which is precisely the embodiment of specific physical law constraints. Mutations in physical systems are not random but are strictly constrained by precisely described theories such as catastrophe theory or critical state theory.

This is a advantage how we use waves to control the world, using a unified multi-perspective 2/3D representation to record the world. Then we use 2D/3D multi-perspective images to connect. 1. The shattering of a cup represents the splitting of one wave and the generation of multiple waves: we record and properly create the unstable points of this system by Wave aggregation and splitting, thus enabling the use of physical laws as constraints. 2. Changes occur only when a wave disappears or is interacted with, and through this, various behavioral rules and effects are learned—this is causality.

### How do we use the principle of least action to organize the core space?

In the core space, we can calculate the volume of waves and simulate relative mass. But in the core space, with thousands of waves, some representing matter, others representing materials or other elements, how do we calculate such complex actions? And whose relationships should we calculate? It's like chaos.

For this abstract space, I hypothesize that wave functions representing static worlds or materials are relatively stationary, and only moving wave functions need to be considered. For these moving wave functions, we then apply the principle of least action for verification, greatly reducing complexity.

In fact, physics itself isn't difficult to master. As the blog "05 Relative be in All Things" states, we can easily master physics, just as LLMs naturally master different rules of code and human language. We adopt the "Principle of Least Action" for the final mile of the marathon, to eliminate locally reasonable but actually absurd situations like "floating chairs."

<strong style="color: #666666">Reasons for the recent improvement in physical understanding:</strong> Because some works abandon tokens and adopt the images themselves like flow-based model, even tiny detailed absurdities might be excluded. Some works used prototypes of WSG (add optical flow/depth), which had already eliminated small absurdities, adding complexity to manifolds/representations can make high-dimensional manifolds more capable of representing the world.

### Module Structure and Training Method?

The wave space is like a "black and white space," while the pixel layer is a "colored space"; semantic IDs, identity information, and advanced features may be lost during the conversion process; whether wave function parameters (frequency, amplitude, etc.) can effectively encode this information remains uncertain. This part should be input again during the decoding process, like the same white model, but different designers have different rendering approaches.

Then we have two modules: text to wave space + wave space to pixels. A convenient training strategy is to develop the two modules using two flow models. Within the larger framework, we can either train these two modules in two separate stages, or complete them in a single-stage training. Considering there is no direct text-to-wave space dataset, single-stage end-to-end training is the most reasonable choice:

- Advantages: End-to-end optimization ensures high coordination between the two modules; wave space naturally forms representations beneficial for final pixel generation; the training process is streamlined without intermediate checkpoints; avoids uncertainty in intermediate representations; only requires text-image pair data, which is already widely available.
- Disadvantages: The wave space may not be as interpretable or controllable; difficult to isolate and debug problems in specific modules.

If we are very fortunate and discover that the wave space naturally forms an orderly space that can be understood by humans, then we can export it to various 3D formats through the following methods: 1. Wave function analysis extraction: sample wave function amplitude values, extract iso-surfaces; use Marching Cubes algorithm to convert to mesh. 2. Probability cloud to point cloud: generate point clouds based on spatial probability density defined by wave functions. 3. Direct 3DGS mapping: map wave function parameters directly to 3D Gaussian bodies. 4. Mixed representation converter: train specialized networks to convert wave space parameters to specific 3D formats.

## Question and discussion

### Sen Fang Initialization

Recently (April 14, 2025), I suddenly realized that our wave core space generates pixels through velocity fields, which means the core space effectively replaces random Gaussian noise. This is like an initialization process, as a significant portion of generative models use noise or random pixels for initialization. If we generate content not from random pixels, but through meaningful information tensors (shapes, spatial information, planar structures) for initialization, we could save anywhere from several times to hundreds of times the training and inference time. <strong style="color: #666666">I call this concept "Sen Fang Initialization."</strong>

For the wave core space, I initially conceived it as a carrier for virtual-real conversion, later it evolved into a representation recording multi-perspective views of the world, and later still it became a carrier of physical rules. However, this concept can also be applied to other generative models (other generative models can also have core spaces), and it doesn't necessarily have to be a wave space (other 3D generative models might use meshes). Furthermore, core space is <strong style="color: #666666">a method of 3D/4D initialization that accelerates and optimizes the generation process by providing valuable multi-dimensional information.</strong>

This method actually has strong universality and can be applied to almost all AI domains. Therefore, Sen Fang Initialization deserves to be proclaimed and discussed separately here.

### What is the next generation of entertainment for humans?

Current diffusion models are like monopolistic enterprises. New generative models need to find their own areas that diffusion models cannot do or cannot do well in order to carve out a path. Otherwise, mature community environments like ComfyUI will defeat and conquer them. WaveGen aims to seamlessly process content from 2D to 4D, hoping it can become a complete generation pipeline like 3D rendering to 2D, but completely AI-based.

It can create personal metaverse-like experiences, but whether it can reach the level of popularity depicted in the movie ["Ready Player One"](https://en.wikipedia.org/wiki/Ready_Player_One_(film)) for gaming remains unknown. Perhaps it could first achieve success as a film production base, where we generate many virtual actors performing in WSF, and then adjust camera angles to shoot films. This approach might reach trillion-dollar industry scale more quickly.

Due to its superior world modeling characteristics (diffusion can only achieve about one-ninth to one-third of these characteristics), even if the world generation is not enough to launch a new era, we might be able to secure a position as future infrastructure based on its world understanding capabilities.

For example, in terms of helping embodied intelligence, our most concise conception of a scene is points, lines, and surfaces. When we see city photos, there might be cars moving or stationary, or sudden changes. All of these conform to probability and the principles of core spatial representation. What humans have, the core space also has; the flaws humans have, the core space also has - nothing excessive, just perfectly appropriate.

