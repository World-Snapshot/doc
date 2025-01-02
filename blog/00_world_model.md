# Discuss Real World Models

## What is Real the World Models

Yann LeCun often says that large language models are not world models, and humanity needs something new to reach the next level. Indeed, large language models often make mistakes in the most basic reasoning, and perhaps super-alignment is a direction to enhance Agent intelligence. But LLMs are indeed not world models; in my view, they are just two-dimensional beings.

Fei-Fei Li has also tried to create model-based spatial intelligence to make some improvements. This path has potential but isn't elegant enough. Although data is finetuned simply, it primarily serves the model. Of course, newly developed spatial methods will always be valuable experience and wealth for reference.

Some early works had "world model" in their names, but they were just beneficial attempts with agents and scenarios - these attempts ahead of their time. Because there were no LLMs, agents, or robots trained in excellent simulation environments back then. So from today's perspective, those works were just prototypes that touched the boundaries of hybrid agents and artificial environments. Finally, some works are actually just better image generation models or architectures without touching the essence.

However, some works are quite nonsensical - they're clearly doing Text2Motion or Text2Pose, yet claim to be world models. Where is the "world" in this? Would changing the engine or other visualization environments affect their human pose generation? It would be better to call themselves human model, embodied intelligence rather than world models. City modeling and 3DGS are more qualified to call themselves world models than these works.

## Complex Information's World Representation

Remember Yann have mentioned that:

"A 4-year-old human child has a total of 16,000 hours of wake time, which is equivalent to 30 minutes of YouTube uploads. We have 2 million optic nerve fibers entering our brain, each fiber carrying about 1 byte per second, maybe 0.5 bytes per second.

Some estimates say it's 3 bits per second, but that doesn't matter - it's an order of magnitude. So the amount of data is about 10^14 bytes, roughly the same order of magnitude as LLMs. So in 4 years, a child sees as much visual data or data as the largest LLMs trained on public text across the entire internet."

This makes sense, but he later seemed to expect an architecture more powerful than Transformer to achieve this. But now I believe that perhaps we should start with the data itself. The existing architecture can still exert powerful capabilities.

So, my proposed "World Snapshot Graphics (.wsg)" seems to be the answer many researchers are looking for. LeCun almost reached the periphery of the thin veil, but unfortunately he hoped to develop a new algorithm. Of course, the development of new algorithms based on WSG is still necessary. This can be seen in the next blog post.

**Note1**: I originally only learned about world models through LeCun's tweets, about two or three of them. Actually, I don't care about world models at all, I think it's a very broad concept. But when I recently conceived the WSG format, and then I revisited part of his published speeches. I was surprised - although he didn't provide the answer, but his definition (models that can predict future world states) was sufficient to describe WSG-based models, namely world models.

**Note2**: I later discovered that world models also natively can predict the past world states.

**Note3**: There is an ancient fable: blind men said that the elephant is like a pillar, the elephant is like a pig, the elephant is like a snake - they only grasped part of the thing. Today's researchers are the same, they all explain the world model through their own work, but you can only know the truth by having a broader insight. As for me personally, I prefer to call my model a world snapshot model.

*Conceived this blog on 22th Dec 24, Completed on 23th Dec 24, Updated on 26th Dec 24*

<!--
<div style="background-color: #f5f5f5; box-shadow: 0 4px 8px rgba(0,0,0,0.1); padding: 5px;">
    <p>"A 4-year-old human child has a total of 16,000 hours of wake time, which is equivalent to 30 minutes of YouTube uploads. We have 2 million optic nerve fibers entering our brain, each fiber carrying about 1 byte per second, maybe 0.5 bytes per second.</p>
    <p>Some estimates say it's 3 bits per second, but that doesn't matter - it's an order of magnitude. So the amount of data is about 10^14 bytes, roughly the same order of magnitude as LLMs. So in 4 years, a child sees as much visual data or data as the largest LLMs trained on public text across the entire internet."</p>
</div>
-->