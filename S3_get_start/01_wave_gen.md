# World Snapshot Model v1 (Augustus)


## Overview

World Snapshot Model v1, code-named **Augustus**, is the first large-scale implementation of the Unified Law for Visual Tasks. It does not train RGB generation, depth estimation, pose estimation, material prediction, reconstruction, and conditional control as unrelated systems. It represents each as a generative route from available evidence to a requested World Snapshot target.

The active implementation uses World Snapshot Graphics (WSG), a shared rectified-flow visual backbone, and TunnelingNet. WSG exposes visual and physical variables at the image boundary; TunnelingNet gives each task a small trainable tunnel through one shared generator. A Channel Head identifies one complete task: its input evidence, target, interface type, routing recipe, and deployable parameters.

## Background

### From WaveGen to WSM

WaveGen was the first attempt to answer a useful question: can a generative model represent more of the world than RGB appearance? Its early documents explored analytic wave functions, a continuous core space, view-dependent collapse, and direct manipulation of hidden world variables.

The analytic wave-function architecture was eventually abandoned. Experiments did not justify forcing learned visual structure into a hand-designed family of spherical harmonics or probability clouds. The current system does **not** generate a WSF or a mathematical wave core.

Several underlying ideas survived and became more concrete:

1. **RGB is not the final boundary.** Geometry, motion, pose, material, physics, semantic regions, audio evidence, and structured objects can be first-class targets.
2. **Control should come from information itself.** A depth map, normal map, skeleton, mask, audio feature, or first RGB frame is routed as evidence rather than reduced to a vague text description.
3. **Generation and understanding share one operation.** Changing which variable is observed and which variable is generated changes the task without changing the generative formulation.
4. **Flow is a useful transport view.** The present model uses rectified flow in visual latent space rather than the old analytic wave space.
5. **Internal variables should be observable.** WSG Readers decode non-RGB targets into official visualizations and, where possible, restore physical or semantic units.

The V0 documentation preserves the original WaveGen proposal. This V1 page documents the system that was actually trained and evaluated.

## Theory

### The Unified Law

The central statement is:

> **If all information can be encoded into the image itself, two-dimensional image generation becomes lossless World Snapshot generation.**

“Image” here means an image-like boundary representation, not an ordinary three-channel photograph. A World Snapshot can contain RGB together with aligned descriptions of shape, movement, articulation, material, physical properties, semantic identity, and other observable variables.

A visual task becomes a directed transformation:

`F_k: C_k -> T_k`

where `C_k` is the evidence available to task `k`, and `T_k` is the requested target. Moving a variable from the condition side to the target side defines another task. Adding a modality creates many additional routes, while composing routes creates a Chain of Visual Thought.

### Four Generative Interfaces

The dense task graph is organized by four training interfaces. They are implementation contracts discovered to cover the graph, not a restrictive taxonomy of computer vision.

### A. Estimation and Reconstruction

The current RGB frame is observed and an additional World Snapshot variable is generated:

`RGB_current -> Target_WSG`

Targets include depth, normals, curvature, edges, optical flow, pose, masks, material maps, physical properties, object structure, and audio-related representations. Conventional perception becomes target generation.

### B. Narrow Visual Generation

Text supplies semantic intent, a non-RGB condition supplies structure, and the first RGB frame can preserve appearance:

`(Text, Condition_WSG, RGB_first) -> RGB_current`

Pose-to-person, geometry-guided, and material-guided generation use this route. Broad generation can be composed as text to RGB followed by RGB to another World Snapshot target.

### C. Conditional Control

One additional World Snapshot variable controls another:

`Condition_WSG -> Target_WSG`

Examples include normals to edges, pose to human segmentation, or one physical/material property to another. Cross-modal visual association becomes directly testable.

### D. RGB-Assisted Inverse Rendering

A first RGB frame supplies scene evidence while another observation identifies the current state:

`(RGB_first, Observation_WSG) -> HiddenTarget_WSG`

Appearance evidence often resolves ambiguities that cannot be recovered from a narrow condition alone.

## Idea

### Model Structure: TunnelingNet

A conventional approach would copy and fine-tune a complete generator for every task. TunnelingNet separates the shared visual generator from a task-specific tunnel:

`p_(theta, phi_k)(x_target | x_conditions, prompt)`

Here, `theta` is the frozen FLUX.2 Klein 4B rectified-flow backbone and `phi_k` is the trainable Channel Head for task `k`. The text encoder, VAE, and base transformer remain frozen. A dense tunnel modifies target-side embedding, modulation, attention projections, and feed-forward projections while preserving the shared model.

Each tunnel contains about 12.51M trainable parameters. Separate GPUs can train separate tasks; checkpoints remain independently distributable; and selected Heads can later be assembled into one task bank around the same backbone. The separation exists for training and deployment convenience. Conceptually, the loaded task bank is one World Snapshot Model.

### Two Attention Routes

- **Modality Tunneling Attention (MTA)** serves estimation/reconstruction, conditional control, and inverse rendering. The target keeps its self-attention path and receives a separately normalized target-to-condition path. Clean evidence remains on frozen condition lanes while the task tunnel updates the noised target lane.
- **Native Joint Attention (NJA)** serves narrow RGB generation. Text, target, structural condition, and RGB evidence share the native joint field so RGB synthesis can reuse the backbone's prior.

MTA adds no separate attention parameters. Its contribution is routing: heterogeneous evidence reaches the target directly without retraining every condition lane.

## Further Approach

### Dense and Sparse Tasks

Dense targets naturally fit image-like WSG channels: depth, normals, flow, masks, material fields, and physical maps remain spatially aligned with RGB. They train from normalized latent caches with the shared rectified-flow objective.

Boxes, keypoints, skeleton trees, body parameters, object structures, and audio token sequences are better represented as digitized structures. The **sparse mode** uses task-specific adapters around the same task contract. It does not pretend that every list or tree is a raster image.

This is an important change from early WaveGen. The current system does not force every variable into one mathematical representation. It unifies the **interface and task graph**, while allowing the suitable adapter at the boundary.

### Data, Normalization, and Native Visualization

Training samples intersect the identifiers available for the target and every required condition. A resolved sample contains target and condition latents, optional RGB evidence, caption embeddings, frame position, video identity, and source metadata. This prevents unrelated frames or dataset families from being paired merely because they share a modality name.

Each WSG modality carries a normalization contract. Training uses normalized tensors; export applies the inverse transform before its WSG Reader visualizes or extracts the result. A pseudo-RGB latent is only an intermediate representation and must not replace the official visualization.

Categorical targets add a stricter requirement: spatial support and semantic identity must both be correct. For these tasks, a compact categorical refiner is part of the deployed Channel Head. The final result is generated support followed by category assignment, not an optional post-hoc score correction.

## Implementation

### Training and Execution

Dense and sparse task graphs are stored as JSON configurations. A launcher resolves the Channel Head, task type, modalities, dataset contract, and recipe, then writes the runtime configuration beside the run. Dense Heads use AdamW over tunnel parameters, bfloat16, optional gradient checkpointing, gradient clipping, deterministic validation grids, best-checkpoint tracking, and WSG-native previews.

Runs are stored by Channel Head and experiment. The recommended-model registry chooses the official run; inference selects the best base checkpoint inside it and loads its categorical refiner when required. This prevents a newer ablation or longer but inferior run from silently replacing the released model.

## Discussion

### Visual Chains

A single Head performs one directed task. Multiple Heads can be composed:

`Text -> RGB -> Depth -> Normals -> Edge`

Intermediate World Snapshots are inspectable rather than hidden reasoning tokens. A chain can be edited, evaluated, replaced, or branched at any step. This is the practical descendant of the old “core space” intuition: intermediate world variables are exposed at the boundary and can participate in further generation.

## Prospect

### What Remains from the Original Inspiration

The original documents asked for a world representation that was generative, bidirectional, controllable, modular, and able to reveal more than appearance. WSM v1 realizes those goals through WSG, rectified flow, directed task interfaces, and task tunnels—not through literal quantum wave functions.

The abandoned equations remain useful as design history: they show why editable internal variables, reversible transport, variable routing, and an observable world boundary mattered from the beginning. The current implementation keeps those ambitions while grounding each claim in trainable routes, held-out inference, native visualizations, and deployable checkpoints.
