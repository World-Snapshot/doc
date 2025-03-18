# Model Design Guideline Memo

Here I write down my design creation thoughts to help readers better understand why I designed the new model this way. It will help future researchers quickly get started with, use, and improve this model.

## Overview

First, I want to train the entire world, with the key being making the data closer to the world's reality. To train the world itself, I created WSG.

Then, I hope to accelerate training efficiency, as training a real world is too resource-intensive (not those fake world models: i.e., video generation models). Therefore, I considered using quantum wave functions - their mathematics is elegant and is nearly capable of truly describing the world.

Next, I want to create a model that can unify 1D, 2D, 3D, 4D, and other dimensions, because training a world naturally means training the all dimension, and the new principle inherently allows for it. I'm designing a completely new model from top to bottom, just like Mendel's peas.

The basic WaveGen has no attention mechanism, just like the original diffusion model paper. It consists of a text encoder module that can understand prompt inputs and a Wave generation module. But temporal continuity is important: although the wave equation itself supports time as a parameter, we need to use frame-to-frame parameter learning to make the world field generation more smooth, like vertical and horizontal road. Also, even if the generated local video segments are consistent, we cannot guarantee that the semantics of the entire video are consistent.

So what should I choose for Temporal Attention? I decided to use RWKV, the best existing linear attention RNN model, abandoning Transformer. Just as the symmetric U-Net was incorporated by diffusion models years later, I believe RWKV and WaveGen are a perfect match - they have too many mutually beneficial properties.

For training strategies, we know there are broadly two categories: self-supervised MSE and reinforcement learning. I lean towards using pure reinforcement learning to train this next-generation new model born in 2025, because for prompt inputs, images themselves are inherently uncertain. Just like DeepSeek-R1 in 25 year, letting the model learn by itself might be more liberating, and RNN states are denser, naturally suited for RL. Moreover, RNN is suitable for causal learning, more elegant than NVIDIA's video generation model named Cosmos in 24 year.

I considered using the seq2seq concept (since our images contain pose information, it like leaves have veins, with stronger constraints), but it doesn't seem very compatible with RNN. I'm also considering MSE as my backup/mixed training strategy.

This sets the tone for the entire new model.

## Doubt

