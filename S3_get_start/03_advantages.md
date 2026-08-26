# WSM v1 and TunnelingNet: Design Advantages


## Overview

WSM v1 is designed around a different unit of scale. Instead of asking one model to expose one fixed prediction API, it asks a shared generator to produce whichever World Snapshot target a selected task requests. Classification, localization, detection, segmentation, estimation, reconstruction, generation, rendering, and control can therefore share a generative interface while preserving the representation each target needs.

Its advantage is not that every historical vision architecture should be discarded. It is that many previously separate tasks can be trained, deployed, composed, and inspected within one directed system.

## 1. Representation

| Design | Primary boundary | Typical task organization | Adding a task |
|---|---|---|---|
| RGB generator | RGB image/video | generation endpoints | change conditioning or retrain |
| Discriminative foundation model | embedding/tokens | fixed prediction heads or prompts | add a decoder/head |
| Monolithic multi-task model | shared features | predefined output heads | change the joint model |
| **WSM v1** | **World Snapshot variables** | **directed generative task routes** | **train a compact tunnel or sparse adapter** |

WSG makes many targets spatially explicit. Depth, normals, flow, pose, masks, material fields, and physical maps remain aligned with the image boundary. Sparse mode covers structures that should remain lists, trees, parameters, or token sequences.

This combination avoids two extremes: reducing every target to opaque tokens, or forcing every structured target into a pseudo-image.

## 2. Task Scaling

One Channel Head corresponds to one selectable task. The shared backbone learns a broad visual prior; the Head learns how a particular set of conditions reaches a particular target.

A new aligned modality creates more than one capability. It can become:

- a target estimated from RGB;
- a condition for RGB generation;
- a condition for another World Snapshot target;
- evidence in RGB-assisted inverse rendering;
- an intermediate node in a visual chain.

The marginal training cost is the tunnel rather than another full backbone. Independent Heads can be scheduled across GPUs, tested independently, and later loaded around the same generator.

## 3. Evidence Routing

TunnelingNet does not concatenate every condition indiscriminately. Its two attention routes reflect a useful experimental finding.

**Native Joint Attention** preserves the backbone's RGB synthesis behavior when the target is RGB. **Modality Tunneling Attention** gives a non-RGB target a direct, separately normalized path to clean evidence. This reduces the burden on a small task tunnel: it need not rediscover how to carry the condition through an unrelated noisy target stream.

Multiple conditions remain separate lanes. First-frame RGB, current RGB, WSG conditions, references, and audio can therefore have different meanings even when they coexist in one task.

## 4. Modular Training, Unified Deployment

The physical checkpoint layout is modular because modularity makes thousands of experiments manageable. It does not imply thousands of unrelated full models.

- the backbone is shared and frozen;
- each dense task adds a compact target-side tunnel;
- sparse tasks add their native adapter;
- categorical tasks include a compact semantic refiner;
- the recommended registry binds each released task to its official run;
- ControlWorld presents the assembled routes as one model interface.

This makes failure local. Improving one weak target does not require retraining every successful task, and a new task can be distributed as a small incremental artifact.

## 5. Observable Visual Reasoning

A conventional model may hide intermediate reasoning in activations or text tokens. A WSM visual chain exposes intermediate targets as World Snapshots:

`RGB -> Depth -> Normals -> Edge`

Each step can be visualized with the official reader, measured against ground truth, replaced by another Head, or manually edited before the chain continues. The chain is therefore both a computation and a diagnostic record.

## 6. Current Scope

WSM v1 validates its law and architecture over more than one thousand trained visual tasks and supports thousands of task definitions. It is a research system rather than a claim that every route has equal evidence or equal maturity.

Some mappings are naturally strong because their input contains the requested information. Others are ambiguous, weakly supervised, categorical, or limited by automatically constructed labels. The graph makes these differences visible instead of hiding them behind one aggregate score. Its modular design also turns every weak route into a precise upgrade target.
