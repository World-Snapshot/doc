# Discuss Real World Models

*"I now define the frame of the System of the World Models." -- SF*

## What is Real the World Models

[Yann LeCun](http://yann.lecun.com/) often says that large language models are not world models, and humanity needs something new to reach the next level. Indeed, large language models often make mistakes in the most basic reasoning, and perhaps super-alignment is a direction to enhance Agent intelligence. But LLMs are indeed not world models; in my view, they are just two-dimensional beings.

[Fei-Fei Li](https://profiles.stanford.edu/fei-fei-li) has also tried to create model-based spatial intelligence to make some improvements. Both the image generation model and the spatial understanding model are studied. Although model and data is finetuned simply to construct the spatial, it primarily serves the model. Of course, newly developed spatial methods will always be valuable experience and wealth for reference.

Some early works had "world model" in their names, but they were just beneficial attempts with agents and scenarios - these attempts ahead of their time. Because there were no LLMs, agents, or robots trained in excellent simulation environments back then. So from today's perspective, those works were just prototypes that touched the boundaries of hybrid agents and artificial environments.

Finally, some works of big company or famous lab, despite extensive promotion and contributions, are merely better image generation models or architectures. There is no fundamental change in their essence, so they are no different from image generation ten years ago, just with better results.

However, some works are quite nonsensical - they're clearly doing Text2Motion or Text2Pose, yet claim to be world models. Where is the "world" in this? Would changing the engine or other visualization environments affect their human pose generation? It would be better to call themselves human model, embodied intelligence rather than world models. City modeling and 3DGS are more qualified to call themselves world models than these works. (see Note6)

## Complex Information's World Representation

Remember Yann have mentioned that:

"A 4-year-old human child has a total of 16,000 hours of wake time, which is equivalent to 30 minutes of YouTube uploads. We have 2 million optic nerve fibers entering our brain, each fiber carrying about 1 byte per second, maybe 0.5 bytes per second.

Some estimates say it's 3 bits per second, but that doesn't matter - it's an order of magnitude. So the amount of data is about 10^14 bytes, roughly the same order of magnitude as LLMs. So in 4 years, a child sees as much visual data or data as the largest LLMs trained on public text across the entire internet."

This makes sense, but he later seemed to expect an architecture more powerful than Transformer to achieve this. But now I believe that perhaps we should start with the data itself. The existing architecture can still exert powerful capabilities.

So, my proposed "World Snapshot Graphics (.wsg)" seems to be the answer many researchers are looking for. LeCun almost reached the periphery of the thin veil, but unfortunately he hoped to develop a new algorithm. Of course, the development of new algorithms based on WSG is still necessary. This can be seen in the next blog post and Standard.

However, it's important to note that <strong style="color: #666666">top researchers are actually pursuing several types of things:</strong> 1. Models beyond LLMs that can truly reason. 2. New models that can truly understand, interact with, and control (which can be divided into two major categories: generation and understanding - the former being 3D information-rich world generation, and the latter being embodied intelligence, spatial understanding, automatic driving and action output of VLM/Agent). 3. The sustainable learning of model. 4. Truly memorize and use part of knowledge. My work can only address the second problem: generating or understanding a more reasonable, editable, and explicit world.

Many people are confused and can't distinguish the future direction, they don't even know which category their work belongs in.

**Note1:** I originally only learned about world models through LeCun's tweets, about two or three of them. Actually, I don't care about world models at all, I think it's a very broad concept. But when I recently conceived the WSG format, and then I revisited part of his published speeches. I was surprised - although he didn't provide the answer, but his definition (models that can predict future world states) was consistent with three ninths of the definitions/natures of the WSG-based models, namely world snapshot models.

**Note2:** I later discovered that world snapshot models also natively can predict the past world states. 

## Definition

I combine people's opinions<sup class="footnote" data-note="After starting my work, I read some public discussions by researchers regarding the definition of the world model.">1</sup> to make the following definition, a world snapshot model or ideal world model should generate:

- **Spatial sequence (x,y,z):** For modeling geometric space.
- **Time sequence (t):** Generate dynamic, static, continuous, discontinuous content with temporal flow (now, past, future).
- **Dense representation:** Texture, lighting, rendering process, as many physical meanings and properties as possible. And all these properties need to be controllable<sup class="footnote" data-note="In fact, controllability can almost be regarded as a new feature, because before ‘wsg birth + virtual-real transformation‘, there was no good method for pixel-level control. Previous work relied on 2D instance methods such as reference images and concept-level control methods such as prompts. While we developed 3-4D instance control and hundreds of condition control at the pixel level.">2</sup>.
- **Semantic instances:** The environment is not a whole, but broken down into specific objects, enabling object-level control and recombination.
- **World heart or world core:** In a core space, using some high-dimensional method to represent the probability distribution of the world, then modeling everything's spatiotemporal distribution by the core. After model, it then output the specific content, object or sample. *WaveGen uses [math function waves](https://world-snapshot.github.io/doc/index.html?page=S3_get_start/01_wave_gen.md) to create the heart of world.*
- **Physical constraint:** In the core space, the abstract representation of objects should be constrained. In our work, this is equivalent to using formulas to convert natural distributions into relative energy and relative density based on probability, which allows for further constraints. *We use the '[Principle of Least Action](https://en.wikipedia.org/wiki/Action_principles)' for constraint.*
- **RIVE:** The internal information of the model's main components is <b>R</b>easonable, <b>I</b>nterpretable, <b>V</b>isualizable, and <b>E</b>ditable.
- **Bidirectional training and inference:** The main components can pass information to each other, the model can be used for world generation and understanding, and thus can be plugged into a larger complex model as a module.
- **All living animals have posture information:** Waves have their own propagation directions, for example, perhaps in the world core space, there is a moving rectangular probability wave representing the movement of a car. But for more detailed animals, we need to identify their joints.

Models that conform to these definitions (including but not limited to) will be world snapshot models or ideal world models. For definitions, I referenced some online posts, such as [this link](https://zhuanlan.zhihu.com/p/17003931453), this post outlines four definitions: space-time, dense information (without mentioning control), semantics, and bidirectionality. Then I enriched concepts of world core, physical constraint, RIVE, and creature information based on them (I also created control mechanisms that were unprecedented in terms of scope, quantity and dimension). In fact, these definitions are all manifestations of my "encoding all information onto the boundary" approach. This is the way the world snapshot model progresses towards the ideal world model. ("Compression is intelligence" / "predicting the next token" is the method by which LLMs strives for AGI)

**Note3:** Regarding the world core, I will explain it in detail later in the text. Simply put, before output final content, we should use formulas or methods that include parameters (x, y, z, t, ...) to model a spacetime. The specific carrier we use is probability waves (ie, dynamic math functions with shape), while others might also adopt something like deformable meshes as the world core, which similarly falls within the scope of world snapshot models, as long as you follow my path: "encoding all information onto the boundary".

**Note4:** Regarding the physical constraint, I will explain it in detail later in the text. As of 2018, <strong style="color: #666666">all known physical systems</strong> can be explained using the [Principle of Least Action](https://en.wikipedia.org/wiki/Action_principles). ([Cosimo Bambi](https://scholar.google.com/citations?user=W9EMTqIAAAAJ&hl=en), 2018, [Introduction to General Relativity](https://link.springer.com/book/10.1007/978-981-13-1090-4?fbclid=IwAR1nBCT3gYYPl9bs0D8Zi9-S-41iKKHDK0bUvxcD8EUgWNGhUoksQtWykOQ), p. 12) Therefore, as long as it follows this rule, except for slight differences between constants and reality (which can be calibrated through training), the model conforms to physics.

**Note5:** There is an ancient fable: blind men said that the elephant is like a pillar, the elephant is like a pig, the elephant is like a snake - they only grasped part of the thing. Today's researchers are the same, they all explain the world model through their own work, but you can only know the truth by having a broader insight. Time has polluted the concept, therefore, as for me personally, <strong style="color: #666666">I prefer to call my model a world snapshot model</strong>. If when everyone in the future agrees that world snapshot models are the true world models, I don't mind formally calling it a world model.

**Note6:** April 10, 2025: Some researchers/papers believe that world models should have strong capabilities, allowing them to interact with the world based on knowledge in their minds. They are actually envisioning what embodied intelligence (Agent/LLM+Robot) could achieve if it truly understood the world. What they're thinking about is the result of combining world models with some intelligent models. However, this concept is not an ideal world model; it combines LLMs, robotics, and world models—it's an bigger engineering composite. For example, someone believes that world models can make decisions, which is not our definition of world snapshot model or ideal world model.

**Note7:** July 24, 2025: More complex decisions should be the responsibility of LLMs rather than WSMs. However, to be honest, later I did come up with two types of methods for integrating the core space with the real world. Reader can read about WaveGen in the [methods section - Further Approach](https://world-snapshot.github.io/doc/index.html?page=S3_get_start/01_wave_gen.md#core-space-mechanism-and-usage-method). Since the core space represents the evolution of the world, the posture of every world within it can be output externally or be controlled by the outside. Due to the velocity difference between the inside and outside of the world, it can not only create more obvious causality but also output the knowledge that WSMs should have about how the world should be. For example, <strong style="color: #666666">if the model believes that a car should react in a certain way to the outside world, then it should have such a reaction</strong> (Or to put it directly, the core space of WSM can actively or passively synchronize with the outside world. It can be partial synchronization or complete synchronization). Perhaps this is the model decision-making ability that people envisioned in the Note 6.

*Conceived this blog on 22th Dec 2024, Completed on 23th Dec 2024, Updated on 24th July 2025*

<!--
<div style="background-color: #f5f5f5; box-shadow: 0 4px 8px rgba(0,0,0,0.1); padding: 5px;">
    <p>"A 4-year-old human child has a total of 16,000 hours of wake time, which is equivalent to 30 minutes of YouTube uploads. We have 2 million optic nerve fibers entering our brain, each fiber carrying about 1 byte per second, maybe 0.5 bytes per second.</p>
    <p>Some estimates say it's 3 bits per second, but that doesn't matter - it's an order of magnitude. So the amount of data is about 10^14 bytes, roughly the same order of magnitude as LLMs. So in 4 years, a child sees as much visual data or data as the largest LLMs trained on public text across the entire internet."</p>
</div>
-->