# Is the Universe a World Snapshot Model?

While building World Snapshot Models, I gradually encountered a question larger than the model itself:

> **Is the universe also a World Snapshot Model?**

This question does not mean that the universe is literally running our code, nor that it is a neural network hidden behind reality. It asks whether the universe and WSM share the same information structure: a complete world description evolves continuously, while observers can access only partial snapshots rendered at its boundary.

A World Snapshot is not merely a screenshot. It is an addressable collection of variables describing what exists at one moment: appearance, geometry, motion, material, physical properties, relations, and any other information that can be observed or inferred. A World Snapshot Model learns how these variables are generated, transformed, and kept mutually consistent.

If the universe follows a similar organization, then phenomena that appear mysterious from the viewpoint of isolated objects may become simpler from the viewpoint of one globally constrained world representation.

## What Would It Mean for the Universe to Be a WSM?

Let the complete description of the universe at time <i>t</i> be <i>U</i><sub>t</sub>. Its evolution can be written abstractly as:

<code>U_t -> U_(t+1)</code>

An observer does not read all of <i>U</i><sub>t</sub>. The observer obtains a local World Snapshot through a limited reader:

<code>S_(observer,t) = Reader_observer(U_t)</code>

The world and an observation of the world are not the same object. A camera records RGB. A depth sensor records geometry. A human observes only a narrow range of physical signals. Each is a different reader of one shared world.

Under this hypothesis:

- physical fields are variables in the global World Snapshot;
- physical laws are transition and consistency rules over these variables;
- time is the ordered evolution of World Snapshots;
- measurement is a reader producing a locally observable result;
- different observers may read different projections of the same world;
- correlations can be global properties of one representation rather than messages exchanged between independent representations.

This resembles the motivation behind WSG. RGB alone records only the visible surface. WSG expands the boundary so more properties of the same world can be represented together. The universe, if it is an ideal WSM, would contain an incomparably richer variable system and an exact transition rule.

## The Holographic Precedent

This hypothesis is not based only on an analogy invented after WSM. It has a serious precedent in theoretical physics: the holographic principle.

In [“The World as a Hologram”](https://arxiv.org/abs/hep-th/9409089), Leonard Susskind developed the idea that the information contained in a spatial region can be represented on its lower-dimensional boundary. Maldacena later provided the best-known concrete realization through [AdS/CFT](https://arxiv.org/abs/hep-th/9711200): under specific conditions, a gravitational theory in a <i>d</i>+1-dimensional bulk has an equivalent description in a <i>d</i>-dimensional boundary field theory.

World Snapshot follows the same direction of dimensional organization. Instead of explicitly reproducing every dimension of a world as an inaccessible internal object, WSM encodes observable world properties into an <i>N</i>-1-dimensional boundary and learns how those properties are generated, transformed, and kept consistent.

In this sense, WSM is a computational method for constructing a lower-dimensional generative description of a higher-dimensional world. WSG is not merely a richer image format; it is an engineered boundary on which the variables of a world can be recorded and manipulated.

The holographic principle does not prove that the physical universe is literally a WSM. It establishes something more useful for this discussion: **representing an (N)-dimensional world through an <i>N</i>-1-dimensional boundary is a physically serious form of equivalence, not an arbitrary computer-vision metaphor.**

For this reason, a toy computational experiment is unnecessary here. Training a network to reproduce Bell correlations would prove only that the network can fit those statistics. The universe-as-WSM proposal stands or falls on the structural equivalence between world, boundary, observation, and global consistency—not on whether a small simulation can imitate one quantum experiment.

## Global Consistency Before Local Appearance

Computer vision usually begins with local appearance: this pixel belongs to this object, this edge belongs to this surface, and this frame follows the previous frame. WSM reverses the priority. These local observations are outputs of a larger consistent World Snapshot.

The same change of viewpoint may be useful in physics. Two distant observations can be locally separate while still belonging to one global state. Their relationship need not be created after one observation occurs; it may already be part of the complete constraint that defines the state.

This does not require the universe to transmit a controllable message instantaneously. It requires the complete World Snapshot to remain self-consistent whenever a local reader produces an observation.

## Try to Explain Quantum Entanglement and "Spooky Action at a Distance"

Quantum entanglement is one of the strongest tests of the universe-as-WSM hypothesis. If a World Snapshot framework cannot even express non-classical global correlations, it is not a serious candidate for describing the organization of the universe.

### Background

Consider two particles prepared in an entangled state whose total spin is constrained. When the same measurement axis is selected for both particles, their outcomes can be strongly correlated or anti-correlated. Each local result is individually unpredictable, yet the joint statistics follow a precise rule.

Bell's theorem made this distinction testable. Local hidden-variable models satisfy Bell inequalities; quantum mechanics predicts correlations that can violate them. Experiments with entangled photons established such violations, work recognized by the [2022 Nobel Prize in Physics](https://www.nobelprize.org/prizes/physics/2022/press-release/). Bell's original argument is available in [“On the Einstein–Podolsky–Rosen Paradox”](https://cds.cern.ch/record/111654).

The result is often described too casually. Bell tests do not show that one particle sends a controllable faster-than-light message to another. They show that the observed joint statistics cannot be reproduced by the relevant class of locally factorized hidden-variable explanations. Entanglement still obeys the no-signalling constraint: one observer cannot choose an outcome and use it to transmit information instantaneously.

The real puzzle is therefore sharper:

1. the two local outcomes are individually random;
2. their joint distribution is more strongly constrained than a local classical account allows;
3. the constraint appears without a controllable signal travelling between the two measurements.

### My Prediction and Inference

My original intuition was:

> <strong style="color: #666666">“Quantum entanglement or action at a distance occurs at a conceptual level. When I change variables in a wave function, the entire function affects the result. Therefore, I believe quantum entanglement operates at a conceptual level.”</strong>

In a World Snapshot Model, “conceptual level” can be stated more precisely. It is not another physical speed. It is the level at which a relation is defined.

If two values are members of one global variable, their consistency does not require a message to travel from one value to the other. A circle does not inform its opposite side when its radius changes; both sides are constrained by the same circle. Likewise, an entangled pair may be better understood as one jointly defined object with two spatially separated observation interfaces, rather than two complete local objects that later negotiate their results.

The correlation belongs to the representation before it belongs to either observation.

### A World Snapshot Interpretation

Under the WSM hypothesis, an entangled system contains at least three layers:

1. **The global state.** One joint World Snapshot variable describes the entangled system.
2. **The local readers.** Observer A and observer B choose measurement settings and obtain only their local outputs.
3. **The consistency rule.** The joint reader must produce outcomes whose distribution respects the global state, even though neither local reader can inspect or control the other output.

This can be written as:

<code>Global entangled state + local settings -> jointly consistent local outcomes</code>

The important object is the joint conditional distribution:

<code>P(a, b | x, y)</code>

Here, <i>x</i> and <i>y</i> are the two measurement settings, while <i>a</i> and <i>b</i> are the outcomes. A purely local classical explanation attempts to factorize the result through a shared hidden variable λ:

<code>P(a, b | x, y, λ) = P(a | x, λ) P(b | y, λ)</code>

Bell violations show that this locally factorized form is insufficient for the observed correlations. A universe-level WSM would instead treat the pair as one global variable and the two measurements as partial readers of that variable.

This offers a concrete interpretation of “action at a distance”: perhaps there is no action travelling across the distance. The distance exists in the rendered spatial snapshot, while the correlation exists in the global definition from which that snapshot is read.

### Why Macroscopic Objects Look Different

A macroscopic object interacts with an enormous environment. Its useful state becomes distributed across many degrees of freedom, making coherent quantum relationships extremely difficult to isolate and preserve. In WSM language, the object is no longer read through a small clean joint variable; it is entangled with a vast number of surrounding variables.

The analogy is not that neural-network noise causes physical decoherence. The useful structural similarity is that a compact global constraint becomes inaccessible when its information is dispersed across a much larger system.

This may explain why the World Snapshot viewpoint feels natural at the microscopic level but ordinary local objects appear sufficient at the macroscopic level.

## Discussion

The universe-as-WSM hypothesis changes the unit of thought.

If we begin with isolated particles, entanglement looks like an impossible communication problem. If we begin with one globally defined World Snapshot, spatial separation and informational separation are no longer identical. The two observations can be distant in rendered space while remaining components of one state description.

This is also why the question belongs naturally to the World Snapshot project. We did not approach physics merely to borrow its vocabulary. We built a model around boundary encoding, explicit world variables, generative transformation, and global consistency. The physical universe is the largest possible case of the same representational question.

Perhaps the universe is not assembled from independently existing local pictures. Perhaps every local picture is a partial reading of one evolving World Snapshot Model.

*Conceived this section on 19th Jan 2025; reframed under the World Snapshot Model hypothesis on 25th Aug 2026.*
