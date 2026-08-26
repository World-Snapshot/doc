# Advanced Features


A central design direction in WSM is to expose useful intermediate variables without claiming that every variable in nature is already observed. WSM makes a growing set of useful intermediate variables explicit at the image boundary so they can be generated, inspected, edited, and reused.

## Explicit Intermediate World Snapshots

Geometry, motion, pose, material, physical attributes, semantics, and structured objects can become visible endpoints. A model can expose what it inferred instead of keeping every intermediate decision inside an opaque latent state.

## Chains of Visual Thought

A generated target can become the condition of another task. This supports longer visual programs, counterfactual edits, cross-checks, and alternative routes to the same target. Because every intermediate result is inspectable, failures can be localized to a particular transformation.

## Extensible Modality Vocabulary

Adding an aligned modality expands both the node vocabulary and the possible directed tasks. The dense graph handles image-like variables; sparse mode provides the extension point for structures whose native form is not an image.

## Task-Local Improvement

A weak task can receive a better dataset, tunnel, adapter, loss, or categorical refiner without disturbing successful routes. This gives WSM incremental and continual growth at the task level.

## ControlWorld Composition

ControlWorld turns these features into an interactive interface. Users can select a graph edge, provide all required evidence, inspect native legends and outputs, and move a generated World Snapshot into the next route.
