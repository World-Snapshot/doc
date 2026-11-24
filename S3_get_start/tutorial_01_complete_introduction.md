# Tutorial 1: Visual-Task Unification and World Snapshot Models

I wrote this tutorial so that anyone can understand what happened without reading the paper, examining the results, or inspecting the code.

## Background: Two AI Fields, Two Different Outcomes

Two of the largest areas of AI are computer vision (CV) and natural-language
processing (NLP). CV has approximately 1,400 tasks, while NLP has approximately
900 tasks.

With the emergence and large-scale commercialization of large language models,
a user can enter a few sentences and ask one model to perform essentially any
NLP task in a prompt--answer form. In this sense, <strong class="tutorial-emphasis">NLP tasks have been unified</strong>
under a common model paradigm.

In general, if the input or output of a task contains a visual element, it can
be classified as a visual task. Unlike NLP, however, visual-task forms and data
formats are complex and cannot be reduced to a simple prompt--answer format.

Visual-task forms include classification, localization, detection,
segmentation, estimation, reconstruction, tracking, editing, rendering,
simulation, planning, and many others.

Visual data also have many different distributions. An image is only a way of
visualizing data, not a universal representation of data. Some visual data even
have special abstract constraints and specifications.

Text, by contrast, is still text. Even relatively structured information or
code in formats such as SQL, Word, and Excel remains text or a string.

As a result, <strong class="tutorial-emphasis">computer vision still lacks a general method or single model</strong> that
can easily perform all of its tasks. Since the emergence of large language
models, this gap has become increasingly consequential for the direction of the
field and for the work of computer-vision researchers.

## Three Goals of Visual-Task Unification

Our work therefore addresses <strong class="tutorial-key">three goals</strong>, with three corresponding solutions:

1. <strong>Unifying visual-task forms.</strong> This is addressed by the Unified Law, a conceptual solution that organizes visual tasks into four generative interfaces.

1. <strong>Unifying visual input and output formats.</strong> This is addressed by World Snapshot Models and World Snapshot Graphics. WSM provides four training interfaces and their corresponding strategies, while WSG unifies the data format.

1. <strong>Unifying training objectives across visual tasks.</strong> This is addressed by TunnelingNet. Every visual task takes a generative form and produces each type of visual or world information in the form appropriate to that task, while only slightly deflecting the original generation path.

The three solutions form one connected sequence: the Unified Law defines the
shared task form; WSM and WSG define the interfaces and world-information
representation; and TunnelingNet provides the common learning mechanism.

## Why Large-Scale Visual Unification Remains Difficult

The approximately 900 NLP tasks have relatively consistent task forms,
training objectives, and formats. Visual tasks take far more diverse forms;
their objectives can point in different or even opposite directions, and their
formats are inconsistent. Even so, vision researchers have attempted several
degrees of unification:

1. Some methods train visual any-to-any systems from scratch or predict visual information as an LLM predicts text through end-to-end multimodal learning. The number of modalities grows slowly because the required data are enormous and can increase almost exponentially. Adding a new visual target may also interfere with existing capabilities.

1. Training one model from scratch to predict all kinds of visual information usually fails to scale. Text tasks can reinforce one another because their format is uniform, whereas visual targets can be different or substantially conflicting.

1. Under these conditions, existing systems usually dedicate one model to one visual task or unify only a comparatively small group of tasks under one method. <strong class="tutorial-emphasis">No existing visual model has unified thousands of visual tasks.</strong>

In other words, the visual world contains more task types, yet those tasks are
harder to unify. The textual world reached a common large-model paradigm first;
computer vision did not.

## Current Methods and a Sixth Paradigm

In practice, stronger visual capabilities are usually built on an existing
backbone through one of <strong class="tutorial-key">five major extension paradigms</strong>:

1. <strong>[ControlNet](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html):</strong> add a new backbone-sized branch and train it to control an existing model;

1. <strong>[LoRA](https://openreview.net/forum?id=nZeVKeeFYf9):</strong> modify a small number of low-rank parameters to change the behavior of the overall model;

1. <strong>[MoE](https://arxiv.org/abs/1701.06538):</strong> add knowledge or computation blocks and route inputs among them;

1. <strong>[IP-Adapter](https://arxiv.org/abs/2308.06721):</strong> train an adapter that coordinates conditioning components inside a model; and

1. <strong>[IC-Control-style methods](https://arxiv.org/abs/2410.23775):</strong> organize text and visual elements in one context so that different visual elements can interact.

These five paradigms commonly extend or improve a particular visual capability
and can be applied to many kinds of visual generation backbones. They describe
where a capability is added and how it influences the existing generation
process.

<strong class="tutorial-key">Our approach constitutes a sixth paradigm.</strong> All six can build on a generative
backbone, but they differ in where a visual capability is added, how it changes
generation, and what constitutes one unit of visual-task expansion.

![Six paradigms for extending visual capabilities](S3_get_start/assets/tutorial/six_extension_paradigms.png)

**Figure 1. A tutorial comparison of six paradigms for extending visual capabilities.** [ControlNet](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html) adds a copied control body; [LoRA](https://openreview.net/forum?id=nZeVKeeFYf9) adds low-rank weight updates; [MoE](https://arxiv.org/abs/1701.06538) selects expert computation; [IP-Adapter](https://arxiv.org/abs/2308.06721) adds an image conditioning branch; [IC-Control-style methods](https://arxiv.org/abs/2410.23775) organize conditions, references, and targets in a shared context; TunnelingNet applies task-specific tunneling forces at multiple depths to redirect a frozen backbone's native RGB trajectory toward a selected target modality.

Figure 1 uses one visual notation to compare six
paradigms. Gray denotes existing or frozen computation, orange denotes added or
trainable computation, blue denotes condition evidence, and purple denotes the
generation target. The figure is deliberately simplified: it shows the defining
information route of each paradigm rather than every implementation detail.

<strong class="tutorial-term">ControlNet.</strong>
[ControlNet](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html) copies a large part of a pretrained generative
network and injects its features into the frozen backbone at multiple depths.
This produces strong and mature spatial control. Its defining unit of extension
is a substantial control body associated with a condition, usually while the
generation target remains RGB. Scaling to many independently maintained
capabilities therefore adds a correspondingly large collection of control
structures.

<strong class="tutorial-term">LoRA.</strong>
[LoRA](https://openreview.net/forum?id=nZeVKeeFYf9) expresses a model update through low-rank matrices. It is
parameter efficient, general, easy to train, and easy to distribute. A LoRA can
learn a cross-modal conversion when its training setup provides the appropriate
inputs and targets. However, LoRA itself specifies how weights change; it does
not by itself define which world information is the condition, which modality
is the target, how clean evidence enters, or how one converted result becomes
evidence for the next task. If the host model retains native joint attention,
heterogeneous prompt, condition, reference, and target tokens continue to share
the same interaction route.

<strong class="tutorial-term">Mixture of Experts.</strong>
[MoE](https://arxiv.org/abs/1701.06538) ([recent review](https://arxiv.org/abs/2507.11181))
increases model capacity by routing tokens to selected experts. Its central
question is which computation or knowledge block should process an input.
Experts and routers can support large models, but adding many visual targets can
increase expert capacity, routing complexity, and coordinated-training cost.
Expert selection alone also does not define a directed graph among visual world
states.

<strong class="tutorial-term">IP-Adapter.</strong>
[IP-Adapter](https://arxiv.org/abs/2308.06721) introduces an image encoder, projection, and
additional attention branch so that image prompts can complement text
conditioning. It provides a strong image-prompt interface while preserving the
pretrained text-to-image prior. Its principal role is to add an external image
condition to RGB generation, rather than to define a large graph of arbitrary
condition--target modality relationships.

<strong class="tutorial-term">IC-Control style.</strong>
In-context visual control methods, including [In-Context LoRA](https://arxiv.org/abs/2410.23775), [ICEdit](https://doi.org/10.52202/085713-4646), [LoRAShop](https://doi.org/10.52202/085713-5596), and [Long Context Tuning](https://doi.org/10.1109/ICCV51701.2025.01605),
place text, conditions, references, and targets into a common context. Their
strength is flexibility: contextual examples can describe a task without a
separate handcrafted interface for every interaction. As more modalities are
added, however, sequence length and joint-interaction cost grow, and new tokens
can change the shared attention field. Conditions and targets are jointly
represented rather than being organized as independently managed directed
routes.

<strong class="tutorial-key">TunnelingNet.</strong>
TunnelingNet treats every target modality as a space that is genuinely
generated. Every condition--target relationship is a visual task with
a target trajectory, evidence route, task key, and lightweight target-side
tunnel. Small task-specific tunneling forces are applied repeatedly through the
depth of the frozen generative backbone, gradually deflecting its original RGB
generation trajectory toward the selected target modality. Clean conditions
act on the noised target through an evidence route. MTA normalizes target
self-generation and condition evidence separately, while NJA remains available
for tasks in which full native interaction is useful.

An intuitive comparison is that TunnelingNet internalizes the layer-wise
steering effect of ControlNet but uses ultralight tunneling paths inside the
backbone instead of attaching a copied backbone-sized branch outside it. The
result is not merely a smaller control module. The tunnel also has an explicit
semantic role in a task graph: it identifies a target, receives specified
evidence, follows a selected attention topology, and can be activated by a task
key. Under the parameter-matched comparison in this paper, this routing reaches
the selected structured outputs with <strong class="tutorial-result">$19.0$--$38.5\times$ fewer updates</strong> and
<strong class="tutorial-result">recognizable target structure $77$--$100\times$ earlier</strong> than LoRA NJA.

## A Detailed Comparison of the Six Paradigms

The compact drawing in Figure 1 becomes more
informative when each paradigm is examined along the same system dimensions.
Table 1 reconstructs that comparison. It is
not a ranking in which one method must replace all others: each established
paradigm solves an important problem. The comparison identifies the additional
organization required when the goal changes from adding one capability to
building a large, directed, maintainable capability system.

<div class="tutorial-table-scroll">
<table id="tutorial-six-paradigms-table">
<caption><strong>Full tutorial comparison of six paradigms for extending visual capabilities.</strong> The rows distinguish an architectural primitive from a complete task-system organization.</caption>
<thead><tr><th><strong>Dimension</strong></th><th><strong class="tutorial-term"><a href="https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html">ControlNet</a></strong></th><th><strong class="tutorial-term"><a href="https://openreview.net/forum?id=nZeVKeeFYf9">LoRA</a></strong></th><th><strong class="tutorial-term"><a href="https://arxiv.org/abs/1701.06538">MoE</a></strong></th><th><strong class="tutorial-term"><a href="https://arxiv.org/abs/2308.06721">IP-Adapter</a></strong></th><th><strong class="tutorial-term"><a href="https://arxiv.org/abs/2410.23775">IC-Control style</a></strong></th><th><strong class="tutorial-key">TunnelingNet / WSM</strong></th></tr></thead>
<tbody>
<tr><td><strong>Method level</strong></td><td>Large auxiliary control architecture</td><td>Parameter-efficient weight update</td><td>Conditional-computation and capacity architecture</td><td>External image-conditioning adapter</td><td>Joint visual-context organization</td><td>Condition--target task architecture spanning representation, routing, trajectory deflection, training, and deployment</td></tr>
<tr><td><strong>Intuition</strong></td><td>Copy a large control body beside the backbone</td><td>Attach a small numerical patch to selected weights</td><td>Add experts and route tokens among them</td><td>Attach an image-prompt branch</td><td>Place text, conditions, references, and target in one context</td><td>Open a small target tunnel inside a shared backbone and steer its generation path repeatedly through depth</td></tr>
<tr><td><strong>Main modification site</strong></td><td>Copied multi-layer network with injections into the backbone</td><td>Weight-side branches of selected linear, attention, or feed-forward layers</td><td>Expert layers and routers</td><td>Image encoder, projector, and adapter attention</td><td>Input sequence, joint attention, and associated fine-tuning layers</td><td>Target-side tunneling paths plus a dedicated condition-to-target evidence route</td></tr>
<tr><td><strong>Added structure</strong></td><td>Near-backbone-scale control body and injection links</td><td>Low-rank matrices $A$ and $B$</td><td>Expert networks and router</td><td>Image encoder, projector, and adapter attention</td><td>Context organization, usually with fine-tuning or LoRA</td><td>Task tunnel, task key, condition--target roles, interface type, and evidence routing</td></tr>
<tr><td><strong>Backbone treatment</strong></td><td>Usually frozen</td><td>Original weights usually frozen</td><td>Implementation dependent; experts and routing are coordinated</td><td>Usually frozen</td><td>Shared model or LoRA is commonly fine-tuned</td><td>Generative backbone, text encoder, and VAE are frozen</td></tr>
<tr><td><strong>How conditions enter</strong></td><td>A copied control body extracts features and injects them layer by layer</td><td>Uses condition interfaces already present in the host architecture</td><td>Router assigns tokens to experts</td><td>Independent image-conditioning branch enters attention</td><td>Condition and target tokens interact in a common context</td><td>Clean evidence acts on the noised target through a declared evidence route</td></tr>
<tr><td><strong>Meaning of a visual task</strong></td><td>Usually a new spatial condition for an RGB target</td><td>Defined by the training data; LoRA itself defines weight change, not an input--output task</td><td>Defined jointly by the shared objective and expert roles</td><td>Usually image prompt plus text to RGB</td><td>A contextual relation learned among jointly represented tokens</td><td>Every input--target mapping has its own generation trajectory, TunnelingNet, and task key</td></tr>
<tr><td><strong>Information route</strong></td><td>External control route through copied layers and injections</td><td>Network topology and token routes normally remain those of the host model</td><td>Router selects computation modules</td><td>Independent image-prompt route</td><td>Shared context provides joint interaction</td><td>Target self-generation is separated from condition evidence; the interface selects MTA or native joint attention</td></tr>
<tr><td><strong>Attention resources</strong></td><td>Control features are extracted before backbone injection</td><td>Under native joint attention, heterogeneous tokens share one Softmax budget</td><td>Tokens compete for or receive routing capacity</td><td>Text and image conditions commonly use separate attention before fusion</td><td>All tokens interact in the shared attention field</td><td>MTA separately normalizes target self-generation and condition evidence; NJA remains available when full interaction is useful</td></tr>
<tr><td><strong>How output changes</strong></td><td>Strong layer-wise control of RGB generation</td><td>Low-rank change to model function without explicit task routing</td><td>Selected experts provide different computation or knowledge</td><td>Image prompt augments text conditioning</td><td>Joint context learns relationships among all elements</td><td>Small task-specific tunneling forces progressively redirect the shared RGB trajectory into a selected target space</td></tr>
<tr><td><strong>Unit of expansion</strong></td><td>Copied control body and injection links</td><td>Set of low-rank weight differences</td><td>Expert capacity and routing</td><td>Adapter or conditioning interface</td><td>Contextual task organization and its training</td><td>Task relation jointly defined by conditions, target, interface, TunnelingNet, and task key</td></tr>
<tr><td><strong>Typical range</strong></td><td>Depth, edge, or pose to RGB</td><td>Depends on data and objective</td><td>Depends on expert definitions</td><td>Image prompt and text to RGB</td><td>Text and visual contexts to a visual target</td><td>Directed generation among appearance, geometry, pose, motion, material, physical, semantic, sparse, and audio information</td></tr>
<tr><td><strong>Adding a capability</strong></td><td>Adds another substantial control body</td><td>Adds an independent patch, but native information routes remain</td><td>May require coordination with experts and router</td><td>Adds an independent conditioning adapter</td><td>Changes the shared context and may require re-coordination</td><td>Trains and installs one task tunnel without retraining the backbone or existing routes</td></tr>
<tr><td><strong>Capability composition</strong></td><td>External workflow combines control modules</td><td>Switch, merge, or stack weight patches</td><td>Router selects or mixes experts</td><td>Combines image prompt with text and other controls</td><td>Combines evidence inside one context</td><td>One route's decoded output becomes clean evidence for the next declared route, creating executable visual chains</td></tr>
<tr><td><strong>Scaling pressure</strong></td><td>Large control structure per capability</td><td>Separate training and management; native evidence competition may remain</td><td>Expert count, routing, and coordinated-training cost</td><td>Primarily expands image conditioning, not arbitrary modality graphs</td><td>Sequence length, joint-interaction cost, and cross-modality interference</td><td>Small independently trainable tunnels; shared prior, task graph, and chains can expand while one request activates only selected TunnelingNets</td></tr>
<tr><td><strong>Principal strength</strong></td><td>Mature spatial control</td><td>Efficient, general, distributable adaptation</td><td>Scalable conditional capacity</td><td>Strong image-prompt conditioning</td><td>Flexible contextual interaction</td><td>Unified task grammar, world-information representation, target routing, lifecycle management, and composable directed generation</td></tr>
</tbody>
</table>
</div>

## What the Comparison Means

Put simply, natural-language processing now has large language models that
handle <strong class="tutorial-emphasis">approximately 900 language tasks</strong> within a common paradigm. Vision has <strong class="tutorial-emphasis">no comparable model</strong>; existing visual methods generally unify <strong class="tutorial-emphasis">no more than approximately 30 tasks</strong>. The main reason is that visual tasks are harder to
train, use incompatible data formats, and optimize inconsistent objectives.

Training a model from scratch with dozens of input types and dozens of output
types is impractical. LLMs succeeded in part because even code is structured
language: linguistic data are inherently more consistent and easier to train on
than visual data.

Computer vision has therefore largely progressed by adding new capabilities to
existing image and video generation models, and the five paradigms above are
among the most common and effective ways to extend such models.

<strong class="tutorial-key">We take a different approach:</strong> reaching hundreds or thousands of new targets by
deflecting the generation trajectory of a shared backbone. Because visual
information can be represented in image-like form, we call the resulting
representation World Snapshot Graphics, or a World Frame, and the model a World
Snapshot Model. Because the method reuses an existing generative backbone while
opening routes to different targets, the analogy of creating new tunnels
motivates the name TunnelingNet.

## What Constitutes the Unified Capability

No single familiar ingredient is presented as the contribution in isolation.
The essential construction is their organization into a scalable visual-task
system:

- <strong class="tutorial-emphasis">A clear mapping</strong> from conditional world information to target world information;

- <strong class="tutorial-emphasis">Non-RGB world states treated as actual generation targets</strong>;

- <strong class="tutorial-emphasis">Independent addition, replacement, repair, and upgrade of task</strong> capabilities;

- <strong class="tutorial-emphasis">Composable generation chains</strong> among multiple visual tasks;

- <strong class="tutorial-emphasis">Separation between capability-library size and per-request active</strong> computation;

- <strong class="tutorial-emphasis">Target-side tunnels paired with condition-evidence routing</strong>;

- <strong class="tutorial-emphasis">Separate processing of target generation and condition evidence</strong> by MTA when the interface requires it; and

- <strong class="tutorial-emphasis">A large, flexibly composable mapping structure over visual tasks.</strong>

This organization supports uncommon and bidirectional conversions whenever the
modalities are sufficiently related, as well as many-to-one, one-to-many, and
many-to-many contracts. RGB can also serve as additional evidence when a
structural modality alone cannot determine texture, boundaries, material, or
scene details. The resulting interface covers dense continuous fields,
categorical maps, sparse structures, body representations, and audio tokens
without requiring all targets to share one decoder.

The scale numbers in the main paper describe the tasks supported by this unified method. WSM v1 performs <strong class="tutorial-result">1,148 evaluated visual tasks</strong> through one shared visual backbone and 1,148 lightweight TunnelingNets. Each dense TunnelingNet adds <strong class="tutorial-result">approximately 12.51M trainable parameters</strong>, <strong class="tutorial-result">about $0.32%$ of the 3.9B visual backbone</strong>. Its complete resident
visual parameter bank is <strong class="tutorial-result">approximately 18.54B parameters</strong>, including all TunnelingNets and deployed categorical refiners. An ordinary dense request,
however, activates <strong class="tutorial-result">approximately 3.913B visual parameters</strong>: the backbone and one selected TunnelingNet. Copying a 3.9B backbone for every evaluated task would require
<strong class="tutorial-result">approximately 4.48T visual parameters</strong>. Sharing the backbone therefore reduces
this task-library parameterization by <strong class="tutorial-result">about $241\times$</strong> while retaining a dedicated TunnelingNet for every task. The method therefore builds a vast capability network while keeping per-request active computation nearly constant.

## How Parameter and Training Costs Scale with More Capabilities

The qualitative differences above become decisive when capabilities are added
at scale. A dense TunnelingNet contains 12.51M trainable parameters. Under the
representative configurations used in our engineering comparison, the
per-capability parameter or weight-memory increment of established extension
paradigms is approximately the multiple shown in
Table 2. These ratios are
configuration-dependent rather than universal constants, but they expose the
different scaling coefficients of the six paradigms.

<div class="tutorial-table-scroll">
<table id="tutorial-parameter-scaling">
<caption><strong>Illustrative per-capability parameter scale relative to one 12.51M-parameter TunnelingNet.</strong> The comparison uses representative configurations of each paradigm; implementations vary.</caption>
<thead><tr><th><strong>Extension paradigm</strong></th><th><strong>Relative scale</strong></th></tr></thead>
<tbody>
<tr><td><strong class="tutorial-result">TunnelingNet</strong></td><td><strong class="tutorial-result">$1.0\times$</strong></td></tr>
<tr><td>IP-Adapter</td><td>$\sim1.8\times$</td></tr>
<tr><td>IC-Control style</td><td>$\sim4\times$</td></tr>
<tr><td>LoRA</td><td>typically $1$--$8\times$</td></tr>
<tr><td>ControlNet</td><td>$\sim29\times$</td></tr>
<tr><td>MoE</td><td>$\sim300$--$10{,}000\times$</td></tr>
<tr><td>Full fine-tuning</td><td>$\sim312.5\times$</td></tr>
</tbody>
</table>
</div>

<strong class="tutorial-key">A 10,000-capability library makes the scaling difference concrete.</strong> Linearizing the representative increments in Table 2, TunnelingNet adds <strong class="tutorial-result">approximately 125.1B resident parameters</strong>, producing <strong class="tutorial-result">a deployed system with roughly 129B resident parameters</strong> while an ordinary request still activates only the backbone and one selected TunnelingNet. The corresponding increments are about 225B for IP-Adapter, 500B for IC-Control, 125B--1.00T for LoRA, 3.63T for ControlNet, 37.5T--1.25P for MoE, and 39.1T for separate full fine-tuning. At this scale, most alternatives become difficult to train, store, transfer, and repeatedly upgrade. The conclusion is supported by measured experiments, not parameter arithmetic alone. Under matched trainable parameters, TunnelingNet reduces pooled training time by <strong class="tutorial-result">$20.6\times$</strong>; across five representative external tasks, WSM records <strong class="tutorial-result">23 first-place and three second-place results</strong>. The scaling advantage is therefore achieved without trading away task quality. At the ultra-large scale of hundreds to 10,000 capabilities considered here, WSM is the only evaluated approach that simultaneously maintains a manageable resident library, near-backbone active computation per request, rapid capability acquisition, and competitive or leading task quality. These properties make it the most practical currently demonstrated route toward ultra-large, LLM-scale visual capability systems containing hundreds of billions, and eventually trillions, of resident parameters.

Parameter count alone does not explain the acquisition advantage. Our
parameter-matched LoRA NJA and TunnelingNet comparison holds the
trainable parameter count fixed. Across Tasks 003, 275, and 313, the measured
training time falls from 41.58 GPU-hours (1.73 GPU-days) to 2.02 GPU-hours
(0.084 GPU-days), a pooled $20.6\times$ acceleration. Applying the same
measured per-task averages to 1,148 capabilities gives an illustrative
capability-library acquisition cost of approximately 663 versus 32.2 GPU-days,
a reduction of about 631 GPU-days. This extrapolation describes repeated
independent capability acquisition; it is not substituted for the measured
three-task result.

The scale becomes larger under industrial training schedules. [SenseNova-Vision](https://arxiv.org/abs/2607.06560)
reports 50,000 training steps on at least 16 80GB GPUs, whereas the corresponding WSM task uses
1,740 single-GPU updates. Counting GPU-updates gives a conservative workload
proxy of at least
$$
    \frac{50{,}000\times16}{1{,}740}\approx460\times .
$$
If every one of 1,148 capabilities were acquired at that workload, the
illustrative total would be <strong class="tutorial-result">approximately 242,000 GPU-days</strong>, compared with about
<strong class="tutorial-result">526 GPU-days</strong> at the observed WSM task time, saving <strong class="tutorial-result">approximately 241,000 GPU-days</strong>. This is a transparent scale scenario based on published steps and
GPU counts, not a measured SenseNova wall-clock or financial result.

Let $c$ be GPU rental cost in dollars per GPU-hour and $R$ the number of
full capability-library acquisition or upgrade cycles. The corresponding
GPU-rental-equivalent saving in this industrial scenario is
$$
    S(R,c)\approx241{,}000\times24\times c\times R .
$$
At $c=\$2$--$\$4$, one complete cycle is approximately
<strong class="tutorial-result">$\$11.6$--$\$23.2$ million</strong>; ten cycles are
<strong class="tutorial-result">$\$116$--$\$232$ million</strong>; and one hundred hyperscale cycles are
<strong class="tutorial-result">$\$1.16$--$\$2.32$ billion</strong>. The arithmetic explains why the same method can
save only hundreds of thousands of dollars for a small deployment yet reach
tens of millions per full training cycle, and hundreds of millions or billions
under repeated hyperscale development. These estimates exclude data,
annotation, engineering labor, storage, networking, and inference.

The same acceleration also changes an individual research cycle. Using the
measured averages above, 50--100 training runs, including seeds, ablations, and
hyperparameter trials, decrease from <strong class="tutorial-result">approximately 29--58 to 1.4--2.8</strong>
single-GPU days. This saves <strong class="tutorial-result">about 27--55 GPU-days</strong>, or roughly
<strong class="tutorial-result">$\$1{,}300$--$\$5{,}300$</strong> at $\$2$--$\$4$ per GPU-hour, while allowing
results to be inspected and experiments redirected within the same day.

Deployment exhibits a separate saving. Replicating a 3.9B backbone for 1,148
tasks requires approximately <strong class="tutorial-result">4.48T parameters, or 8.96TB</strong> of FP16/BF16 weights.
The complete 18.54B-parameter WSM occupies <strong class="tutorial-result">approximately 37.1GB of weights</strong>, and
an ordinary dense request activates <strong class="tutorial-result">approximately 3.913B parameters, or 7.83GB</strong>
of weights. These are weight-only footprints; runtime memory additionally
contains activations and framework state.

## Capabilities That Emerge at the System Level

The table also reveals why the contribution cannot be reduced to another
adapter or a collection of LoRAs. A weight-update primitive answers how a
parameter is changed. A capability system must additionally specify what
information is the condition, what world state is generated, how evidence
reaches that target, how the TunnelingNet is selected, how TunnelingNets compose, and how one
capability changes over its lifetime. Once these relations are explicit, several
system-level abilities become available together:

- <strong class="tutorial-term">Uncommon, bidirectional, and multi-input/output contracts.</strong> Related modalities can be connected in either direction, and contracts can be one-to-many, many-to-one, or many-to-many instead of being restricted to an external condition that controls RGB.

- <strong class="tutorial-term">Executable visual chains.</strong> A decoded result becomes clean evidence for the next route. This is structurally different from merging weights or selecting experts because the intermediate world state and the next target remain explicit and inspectable.

- <strong class="tutorial-term">Independent capability lifecycle.</strong> A TunnelingNet can be trained in parallel, installed, tested, repaired, replaced, upgraded, or rolled back without changing the shared backbone or previously acquired capabilities.

- <strong class="tutorial-term">Target-specific information flow.</strong> Only the target-side tunnel is optimized. MTA can give target self-generation and condition evidence separate normalization, while native joint attention remains selectable for interfaces that benefit from full interaction.

- <strong class="tutorial-term">Heterogeneous native outputs.</strong> Dense continuous fields, categorical maps, keypoints, boxes, skeletons, body parameters, and audio tokens coexist in one task system without pretending that every output has the same decoder or constraint.

- <strong class="tutorial-term">RGB-assisted recovery.</strong> RGB can accompany an incomplete structural condition when texture, boundaries, material, identity, or scene detail cannot be recovered from that condition alone, creating a distinct family of RGB-assisted inverse-rendering contracts.

## A Practical Mental Model of WSG, WSM, and TunnelingNet

The three names describe different levels of the system.

- <strong class="tutorial-term">WSG is the shared representation.</strong> RGB occupies channels 0--2, while additional channel IDs store other world information. Readers and adapters expose dense maps, categories, keypoints, boxes, skeletons, body parameters, and audio-related targets through their native forms.

- <strong class="tutorial-term">WSM is the unified method.</strong> It combines one shared visual prior and thousands of lightweight TunnelingNets. It can be understood as a computer with many specialized applications installed: all applications share the same operating system, and opening one application activates only the selected application instead of executing the entire library.

- <strong class="tutorial-term">Each TunnelingNet is a lightweight TunnelingNet associated with one visual task.</strong> According to the requested input--output task, WSM activates the corresponding TunnelingNet, which redirects the shared generation path toward its target.

This mental model explains why installing more capabilities need not increase
the active computation of an ordinary task request. A new task trains
only its target-side tunnel, leaving the backbone and existing tunnels
unchanged. Different tasks can be trained independently and in parallel. After
training, a capability can be installed, tested, repaired, replaced, upgraded,
or rolled back without retraining the other TunnelingNets.

<strong class="tutorial-key">Adding one capability.</strong>
Training a new capability has five steps: (1) prepare paired conditions and
targets for the desired conversion; (2) register the target's WSG channel
identity and native reader; (3) select the interface, evidence roles, and task
key; (4) freeze the shared backbone, text encoder, VAE, and existing TunnelingNets while
training the target tunnel; and (5) validate, version, and install the resulting
capability. A later correction repeats only the affected TunnelingNet's training and
validation. This workflow is why the system can acquire capabilities on
different GPUs in parallel and why updating one TunnelingNet does not require a new
joint training cycle for the complete library.

The same organization also explains the role of visual chains. Switching,
merging, or stacking weight patches combines parameters, but it does not by
itself define an executable sequence among visual world states. In WSM, the
output of one task can become clean evidence for the next. A sequence
such as
$$
    \mathrm{RGB}\rightarrow\mathrm{Depth}\rightarrow
    \mathrm{Normal}\rightarrow\mathrm{Edge}
$$
is therefore a chain of explicit visual contracts. Each step has a declared
target and can be inspected, replaced, or reused independently.

## From TunnelingNets to a Visual Capability Operating System

![The computer-vision task tree](S3_get_start/assets/tutorial/wsg_task_graph.png)

**Figure 2. The computer-vision task tree.** RGB lies at the center of a larger visual space, while text and World Information form surrounding nodes. Each directed line is a visual task that can be realized by a TunnelingNet. The complete graph therefore turns computer vision from a collection of isolated models into an explicit network of capabilities that can be selected, installed, and composed.

WSM can be viewed as a computer with many specialized applications installed. The
shared backbone plays the role of a common operating system; each TunnelingNet supplies one application-level capability; and a task key opens only the
capability requested by the user. Installing another capability expands the model, while each request activates only its required TunnelingNet.

ControlWorld turns this model into an end-user workflow. A user selects the
condition and target in the task graph, supplies image, text, reference, or
world-information evidence, executes the corresponding tunnel, views the result
through the target's reader, and may pass that result into the next route. This
supports workflows such as

- RGB $\rightarrow$ depth $\rightarrow$ normal $\rightarrow$ edge;

- RGB $\rightarrow$ roughness $\rightarrow$ base color;

- non-RGB conversions such as normal $\rightarrow$ edge;

- edge, depth, normal, or pose $\rightarrow$ RGB generation;

- first-frame appearance plus current structure $\rightarrow$ a new structural or appearance state; and

- structural evidence plus RGB $\rightarrow$ geometry, material, semantics, pose, or other world properties.

The engineering difference is direct. A conventional pipeline may maintain a
separate depth model, normal model, edge model, pose model, and RGB generator,
plus conversion code between their incompatible formats. WSG gives intermediate
world states stable identities, the shared backbone supplies a common prior, and
task tunnels provide replaceable conversions. The output of one step can be
reused immediately instead of being treated as an accidental by-product of an
opaque end-to-end model.

## Explicit Workflows and an Embedded Task Graph

![Selecting and executing one visual path in ControlWorld](S3_get_start/assets/tutorial/controlworld_selected_route.png)

**Figure 3. Selecting and executing one path from the tree.** In ControlWorld, clicking a trained edge—or selecting its input and output—identifies one directed visual task. This example selects RGB $\rightarrow$ relative depth, accepts the required RGB evidence, loads the recommended TunnelingNet and checkpoint, executes inference, decodes the target through its native reader, and exposes the result and inference log in one workflow.

We construct a virtual, conceptual task network around RGB to facilitate the understanding and management of TunnelingNets. In
ControlWorld, the graph is exposed so that a user can select, inspect, and chain
routes. In a deployed WSM, the same task keys, condition--target roles, TunnelingNets, and readers are managed by a shared execution framework and selected by each request.

This distinction also separates <em>capability acquisition</em> from
<em>capability execution</em>. Visual tasks have different targets and can therefore be
learned independently, even on different GPUs, without placing all modalities,
losses, and targets in one joint training batch. At inference, only the TunnelingNet or
visual chain named by the task key is activated. The library can consequently
grow through distributed acquisition while retaining one shared visual prior
and predictable per-request computation.

An additional research direction follows from this organization. A
self-contained WSM may use one of its own estimated world states as evidence for
a later route, or use an audited chain to construct training signals for a new
route. This is not required by the present evaluation; it is a path toward
recursive visual systems whose intermediate reasoning remains represented as
inspectable world information instead of hidden activations alone.

This organization points beyond a single benchmark. The same capability library
can support richer perception for robotics and digital twins; geometry, motion,
material, lighting, and rendering chains for film and games; pose, shape, and
segmentation routes for digital humans, health, and sports; physical and material
property estimation for manufacturing and logistics; editable product assets for
e-commerce; audiovisual localization and segmentation; and institution-specific
routes for medical, agricultural, satellite, or scientific imagery. They illustrate how a common task grammar and independently trainable routes turn
domain expansion into capability installation instead of complete-system
reconstruction. The measurable quantities are correspondingly concrete:
trainable parameters and updates per new TunnelingNet, time to recognizable target structure,
resident library size, active parameters per request, number of independently
replaceable capabilities, and the length and success rate of executable chains.
