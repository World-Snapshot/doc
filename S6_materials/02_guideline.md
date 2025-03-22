# Model Design Guideline Memo

Here I write down my design creation thoughts to help readers better understand why I designed the new model this way. It will help future researchers quickly get started with, use, and improve this model.

## Overview

First, I want to train the entire world, with the key being making the data closer to the world's reality. To train the world itself, I created WSG.

Then, I hope to accelerate training efficiency, as training a real world is too resource-intensive (not those fake world models: i.e., video generation models). Therefore, I considered using quantum wave functions - their mathematics is elegant and is nearly capable of truly describing the world, countless physics papers also said it's a complete way of describing the world.

Next, I want to create a model that can unify 1D, 2D, 3D, 4D, and other dimensions, because training a world naturally means training the all dimension, and the new principle inherently allows for it. I'm designing a completely new model from top to bottom, just like Mendel's peas.

The basic WaveGen has no attention mechanism, just like the original diffusion model paper. It consists of a text encoder module that can understand prompt inputs and a Wave generation module. But temporal continuity is important: although the wave equation itself supports time as a parameter, we need to use frame-to-frame parameter learning to make the world field generation more smooth, like vertical and horizontal road. Also, even if the generated local video segments are consistent, we cannot guarantee that the semantics of the entire video are consistent.

So what should I choose for Temporal Attention? I decided to use RWKV, the best existing linear attention RNN model, abandoning Transformer. Just as the symmetric U-Net was incorporated by diffusion models years later, I believe RWKV and WaveGen are a perfect match - they have too many mutually beneficial properties.

For training strategies, we know there are broadly two categories: self-supervised MSE and reinforcement learning. I lean towards using pure reinforcement learning to train this next-generation new model born in 2025, because for prompt inputs, images themselves are inherently uncertain. Just like DeepSeek-R1 in 25 year, letting the model learn by itself might be more liberating, and RNN states are denser, naturally suited for RL. Moreover, RNN is suitable for causal learning, more elegant than NVIDIA's video generation model named Cosmos in 24 year.

I considered using the seq2seq concept (since our images contain pose information, it like leaves have veins, with stronger constraints), but it doesn't seem very compatible with RNN. I'm also considering MSE as my backup/mixed training strategy.

This sets the tone for the entire new model.

## Idea

### Why Not Use Grid/Mesh and Decay Methods

Grid/Mesh is suitable for importing into existing software rendering pipelines, but it is not suitable as the simplest expression method: 1. For a basic wave unit, only about a dozen parameters are needed for implementation, while grids require more parameters. 2. Waves are suitable as carriers for various calculations or information; for core space, we hope it is a mathematical incarnation or expression form. 3. Waves can carry some invariants related to pixels, and are suitable for becoming functional execution methods, such as essentially serving as a physics engine. Therefore, grid can only serve as a derived form of wave space. Of course, I look forward to better work to improve the core space, such as perhaps using pure mathematics and abstract topological information to create a complete space.

Regarding decay, the wave function actually comes with a spherical harmonic function, but I removed it. This is because I think we should use a basic wave and then carve out any shape, rather than generating various shaped probability clouds from the beginning. These two methods should be equivalent; I just find it more convenient to handle. In addition, I have also tried using various functions or SDF (Signed Distance Field) methods for decay, but I feel they are not as natural as spherical harmonic functions.

### How to decode or render pixels in real time?

For how to implement decoding generation at the pixel level. I have considered using various generative models including VAE, U-Net, pure decoders, RNN-only, etc., but all seem to be slightly lacking. We know that current models have strong characteristics of mutual learning and fusion. For example, the original diffusion model DDPM contains U-Net, Stable Diffusion added VAE latent space, and its generation end also borrowed some ideas from GANs. Flow-based models are now closely connected with Transformers or autoregressive methods, while stable video diffusion uses technology that combines advantages from multiple approaches.

Therefore, for our generative model, we should choose one that is fastest (because we need to "search" multiple times based on changes in perspective), bidirectional (the definition of an ideal world model), and can provide the longest semantic continuous rendering support (this point cannot be guaranteed, as no one has tried it as of March 20, 2025). After research, I plan to use a flow-based model as the foundation, because flow-based model theoretically supports precise bidirectional generation, and it doesn't even process the image too much (i.e. doesn't extract tokens or use potential space for compression). I love this.

## Question and discussion

### What is the next generation of entertainment for humans?

Current diffusion models are like monopolistic enterprises. New generative models need to find their own areas that diffusion models cannot do or cannot do well in order to carve out a path. Otherwise, mature community environments like ComfyUI will destroy them. WaveGen aims to seamlessly process content from 2D to 4D, hoping it can become a complete generation pipeline like 3D rendering to 2D, but completely AI-based.

It can create personal metaverse-like experiences, but whether it can reach the level of popularity depicted in the movie ["Ready Player One"](https://en.wikipedia.org/wiki/Ready_Player_One_(film)) for gaming remains unknown. Perhaps it could first achieve success as a film production base, where we generate many virtual actors performing in WSF, and then adjust camera angles to shoot films. This approach might reach trillion-dollar industry scale more quickly.

Due to its superior world modeling characteristics (diffusion can only achieve about one-ninth to one-third of these characteristics), even if the world generation is not enough to launch a new era, we might be able to secure a position as future infrastructure based on its world understanding capabilities.

For example, in terms of helping embodied intelligence, our most concise conception of a scene is points, lines, and surfaces. When we see city photos, there might be cars moving or stationary, or sudden changes. All of these conform to probability and the principles of core spatial representation. What humans have, the core space also has; the flaws humans have, the core space also has - nothing excessive, just perfectly appropriate.

