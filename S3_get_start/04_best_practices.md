# Best Practices


A central practical lesson in WSM v1 is not to fuse every modality into one undifferentiated tensor. It is to preserve what each modality means, align it to the same World Snapshot, and route it explicitly as evidence or target.

## Define the Task Before Training

A task contract should specify the input modalities, target modality, interface type, dataset families, normalization, reader, and adapter. A Channel Head index alone is insufficient because dense and sparse graphs can reuse indices and because the same target can be reached from different evidence.

## Preserve Alignment

Intersect sample identifiers across every required condition and the target. For temporal data, preserve video identity and frame position. First-frame RGB, current RGB, and a reference image are not interchangeable.

## Use the Native Representation

Use dense WSG channels for spatial fields and sparse adapters for boxes, keypoints, skeletons, parameters, or token sequences. Do not turn a structured target into a colored image solely to make the loader convenient.

## Validate True Inference

Training previews that mix a ground-truth target with noise are useful for diagnosing convergence, but they do not measure deployment. Select fixed held-out samples, fixed seeds, and the same sampler used by ControlWorld. Decode through the official WSG Reader.

## Deploy the Complete Task

Select the recommended run, then the best checkpoint within that run. If the target is categorical, load its compatible categorical refiner. The deployed result is the complete route, not an intermediate pseudo-color field.
