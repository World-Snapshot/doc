# Model Design Guideline Memo

Here I write down my architectural creation thoughts to help readers better understand why I designed the new model this way. I hope this will help broaden readers' perspectives and contribute to their research taste.

## Overview

First, I want to train the entire world, with the key being making the data closer to the world's reality. To train the world itself, I created WSG.

Then, I hope to accelerate training efficiency, as training a real world is too resource-intensive (not those fake world models: i.e., video generation models). Therefore, I considered using quantum wave functions - their mathematics is elegant and is nearly capable of truly describing the world.

Next, I want to create a model that can unify 1D, 2D, 3D, 4D, and other dimensions, because the new principle inherently allows for it, and training a world naturally means training the all dimension. I'm designing a completely new model from top to bottom, just like Mendel's peas.

The basic WaveGen has no attention mechanism, just like the original diffusion model paper. It consists of a text encoder module that can understand prompt inputs and a Wave generation module. But temporal continuity is important: although the wave equation itself supports time as a parameter, we need to use frame-to-frame parameter learning better, like vertical and horizontal attention (similar to the ancient Chinese saying: up, down, left, right is called space; past and present is called time).

So what should I choose for Temporal Attention? I decided to use RWKV, the best existing linear attention RNN model, abandoning Transformer. Just as the symmetric U-Net was incorporated by diffusion models years later, I believe RWKV and WaveGen are a perfect match - they have too many mutually beneficial properties.

For training strategies, we know there are broadly two categories: self-supervised MSE and reinforcement learning. I lean towards using pure reinforcement learning to train this next-generation new model born in 2025, because for prompt inputs, images themselves are inherently uncertain. Just like DeepSeek-R1 from early this year, letting the model learn by itself might be more liberating, and RNN states are denser, naturally suited for RL. Moreover, RNN is suitable for causal learning, more elegant than NVIDIA's video generation model from early this year.

I considered using the seq2seq concept (since our images contain pose information, like leaves have veins, with stronger constraints), but it doesn't seem very compatible with RNN. I'm also considering MSE as my backup training strategy.

This sets the tone for the entire new model.