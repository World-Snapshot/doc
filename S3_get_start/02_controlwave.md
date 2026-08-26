# TunnelingNet and ControlWorld

<!--*"Wave is all things those worlds need."*-->

## Overview

ControlWave began as the idea of controlling a hidden wave core and its rendered pixel layer. The current implementation no longer contains that wave core. Its practical successor is **ControlWorld**, the reference WebUI for selecting, composing, and running World Snapshot Model tasks.

The original separation survives in a more precise form:

- the **task layer** selects a directed route in the World Snapshot graph;
- the **evidence layer** supplies text, RGB, WSG modalities, audio, or structured conditions;
- the **generation layer** loads the shared backbone and selected TunnelingNet Channel Head;
- the **boundary layer** decodes the target with its WSG Reader and exposes the result.

ControlWorld is therefore not a collection of unrelated demo tabs. It is a visual router for a model whose tasks share one interface.

## Idea

### From Core-Space Control to Task Routing

The early ControlWave document proposed fixing part of a high-dimensional state and generating the rest. WSM v1 implements the useful part without a hand-designed wave state.

For every task, ControlWorld resolves:

`(task type, input modalities, target modality, Channel Head)`

and constructs the corresponding evidence lanes. A modality retains its WSG channel definition, normalization contract, reader, and—where needed—structured adapter.

Control is directional. Depth to RGB is different from RGB to Depth; Normal plus first-frame RGB to Edge is different from Normal to Edge. The same variables participate in different tasks because direction and available evidence are part of the task definition.

### The WSG Task Graph

The WebUI graph is generated from dense and sparse task configurations. Its nodes are modalities; its directed edges are trained or configured tasks. Dense WSG modalities and sparse targets participate in the same graph.

The graph supports two-way interaction:

1. selecting inputs and output highlights the corresponding path;
2. clicking an available edge updates the input signature, target, and compatible checkpoint selectors.

Dense and sparse Heads can reuse numeric indices, so a task is resolved by its full contract and registered run rather than by the integer alone.

The recommended-model registry is consulted first. It stores repository-relative run paths so the configuration works on another machine. A warning status can mark a route whose evidence is weak, training remains incomplete, or categorical reliability needs improvement.

## How to Control a World Snapshot Task

### Supplying Conditions

ControlWorld lays out every input required by the selected signature:

- text;
- current-frame RGB;
- first-frame RGB appearance evidence;
- one or more WSG modality images;
- a native reference image;
- audio or an audio-derived feature;
- a sparse structured condition.

Image inputs share a compact grid instead of consuming one row each. Adding a second or third condition does not require a separate handwritten page.

Uploaded visualizations are converted according to the modality contract. Formal inference uses the same routing semantics as training. A condition preview must not be confused with the normalized latent entering the model, and a target-conditioned training preview must not be confused with true inference.

### Loading a Task

A deployed task consists of the shared backbone and selected Channel Head. ControlWorld resolves the official run from the registry, then chooses the best checkpoint within that run instead of searching all training directories by timestamp.

For categorical outputs, the categorical refiner is an integral part of the task. It can be embedded in a checkpoint or stored in a sibling `categorical_refiner/` directory beside `ckpt/`. The runtime loads the best compatible refiner automatically. If a required refiner is absent, the route should appear incomplete rather than silently return poorly calibrated pseudo-colors.

Sparse tasks load their native adapter and sidecar information similarly. A task package remains self-contained while small refiners can still be replaced independently.

## Basic Generation and Visualization

### Running Inference

The inference sequence is:

1. resolve the graph edge and recommended run;
2. validate every required condition;
3. load the backbone, Channel Head, and required sidecars;
4. encode each condition into its assigned lane;
5. sample the target;
6. invert target normalization;
7. construct the output WSG or structured result;
8. invoke the official target reader;
9. expose every generated artifact in the output list.

When a reader produces multiple visualizations—alternative normal displays, raw values, masks, overlays, or metadata—the UI keeps them as separately selectable outputs. The first suitable visualization is displayed by default.

The inference log below the run action streams worker startup, checkpoint resolution, condition preparation, sampling, decoder output, reader selection, warnings, and errors. A single spinner cannot explain which component of a multi-part task failed.

### Native Legends and Output Meaning

The control panel beside the output is derived from the target modality. Continuous values use the official normalization range and color mapping. Categorical values use their palette definition. RGB outputs have no artificial scalar legend.

If the generated target is RGB, the panel may describe the controlling non-RGB condition. If the target is non-RGB, the target takes priority. Quantiles such as Q1 and Q99 are diagnostic statistics, not semantic legends, and must not replace the WSG definition.

This keeps the WebUI, evaluation output, paper figures, and standalone WSG Reader consistent.

## Implementation

### Plugin Architecture

ControlWorld discovers plugins without requiring their WebUI files at the plugin repository root. A plugin can keep those files inside a `webui/` directory while training code, data utilities, and model implementation remain independently organized.

The WSM v1 plugin owns its configuration, frontend, backend adapter, inference worker, and task-graph logic. ControlWorld supplies navigation, theme, plugin lifecycle, shared layout, and backend registration.

Installation and uninstallation are registry operations. Uninstalling removes a plugin from active tabs and runtime registration but does not delete its source directory. It can return to the installable state without destructive filesystem operations.

Plugins inherit the host typography, spacing, colors, form controls, and light/dark variables by default. Specialized visualizations remain possible, but ordinary controls should look native to ControlWorld.

### Reproducible Evaluation

The evaluator uses the same task resolution, best-checkpoint selection, categorical-refiner loading, normalization inversion, and WSG Reader path as the WebUI. A route that works only in a training preview but fails in true inference is not deployed.

Evaluation is incremental. Each result records its task contract, checkpoint, samples, metrics, and artifacts. Compatible completed results can be reused; a changed checkpoint or contract creates another attempt. Large task banks can therefore be evaluated over several sessions without recomputing unchanged tasks.

## Discussion

### What the Original ControlWave Idea Became

ControlWave imagined manipulating the information from which a world is rendered instead of attaching a separate control network for every visual cue. The current system reaches that goal through explicit World Snapshot variables and directed task routes.

There is no hidden wave file to edit. Instead, depth, normals, pose, masks, material properties, physical attributes, audio conditions, and sparse structures can be selected, generated, inspected, and chained. ControlWorld is the operating surface for those abilities; TunnelingNet makes each route trainable without copying the full model.
