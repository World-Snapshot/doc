# Computer Vision's Rebirth

Our **WSG** (World Snapshot Graphics), **WSV** (World Snapshot Video), **WSF** (World Snapshot Fields) and **WaveGen** (Quantum Wave Function Generation) may promote the birth of some new areas:

### Computer Graphics in WS

Development and learning of WSG, WSV, and other formats, exploring WS principles and algorithms based on line, lighting, and shape representation.

### Physics in WS

For example, our WSG natively supports relative and absolute distances. We can create relative volume and predict relative mass through physics knowledge.

Since most world parameters exist in basic units, we can natively calculate world instances rather than through models learning parts separately for interaction.

### Quantum Wave Function Generation

I have specifically developed a new type of generative model based on quantum wave functions (abbreviated as WaveGen) to better model world information. This new generative model has many advantages - conceptually and theoretically, it is rooted in the fundamental principles of the universe, making it much more elegant than the denoising process of diffusion models. Its control over physical conditions is natively supported, making it more elegant than embedded approaches like ControlNet. 

Personally, I hope its impact will surpass both of these predecessors, and hope it will serve as a bridge for communication between the AI and physics communities.

### WS-Based World Generation Models

Just by changing the data loading suffix from .png to .wsg in text2img models, it becomes a text2world world model, very simple.

Then wsg has dozens or hundreds of properties, which previously might have required countless encoders or multimodal fusion methods, but now doesn't need them at all. You input text and can output information in dozens to hundreds of formats.

### WS-Based Fine-tuning of Generative Models

Theoretically, most of the existing flourishing pre-trained generative models don't need to be retrained. They only need to be fine-tuned on WSG format files of certain scale to generate world segments.

For instance, the latest version of diffusion models generates content that is absolutely very close to reality. After fine-tuning, it can attach various physical properties or additional attributes to the generated content.

The more training it receives, the better the generated additional properties should be. Moreover, it won't affect the original generative capabilities (provided that your training data is equally refined). The additional new attribute generation capability depends on the quality and quantity of our new WSG data.

### WSG, WSV, WSF Data Collection

We temporarily record instantaneous world information through various recognition and perception models. However, we can record WS more accurately through mechanical devices. Such WS data quality is significantly higher.

### Data Mining Based on WSG, WSV, WSF

When we train a text2wsg model, we're actually training a text2world model. It contains dozens of times more information, all of which can be used for analysis.

For instance, we can classify wsg through pose/motion information, classify wsg through depth and sound - the world itself has many characteristics, not just simple labels. This transcends traditional image classification to become world classification.

### Pixel-Level Style Transfer

Suppose you have two wsv files, one with a girl dancing and another with a boy dancing.

Theoretically, you only need to exchange their RGB colors in corresponding body pixel regions while keeping their pose information unchanged to achieve motion transfer.

### WS-Based Human Motion Synthesis

In World Snapshot, when we generate human bodies, it's like shadow puppetry - we generate each layer of the person. From outside to inside, these layers are: surface skin layer (RGB colors), normal human body, depth human body, 3D human body (SMPL/Mesh Human), 2D skeleton structure... and so on.

Since they are trained and generated simultaneously, with pixel-level fusion, correspondence, and binding, what we're actually generating is something with rich layers like a building or a world. Theoretically, if the model generates the building or world correctly, the different layers of the human body should be correct.

For example, when the palm is turned sideways, each finger should conform to the 3D structure, rather than having fingers that appear to have a landslide effect.

### WS-Based Occlusion Estimation

World Snapshot shows promise in reducing the possibility of one dog disappearing when blocked by another dog.

Because if an image has two overlapping dogs, the overlapping portion in the segmentation layer will be labeled as a shared part between the two dog IDs, assigned with two depth values. The depth values will be in a list form, where each item has an ID, and the pixel values of each item are determined by the ID indicating whether this pixel belongs to this item. Similarly, depth values will indicate different layers between two items. For example, one item's depth values might fluctuate between zero and ten, while another item's depth values might fluctuate between ninety and one hundred.

After training, the generative model will also be good at handling overlapping objects. For instance, after generation, our video player can make judgments, determining the depth differences between two objects, then deciding which pixels' RGB values should be displayed.

However, there's an issue here: during training, if an object is occluded, you can't predict its color - you can only judge based on the visible parts that can be observed. We won't try to assign predicted colors to occluded parts. This should be decided by the generative model itself.

This also aligns with our logic - this is how we humans do it too. If the occluded person's arm is wearing red clothing, we humans might guess their entire outfit is red. But it's also possible that the main body of their clothing is blue. This has a kind of Schrödinger's cat feeling to it, which is very interesting. I call this the "World Snapshot Clothing Paradox."

### WS-Based Games

WS is a world with explorable perspectives. If text2img models are replaced with text2wsv and can generate 30 frames per second,

It would be more suitable than diffusion models as an infinite game frame generator, plus it has dozens of extra information like distance, sound, etc.

Or we can let Agents explore in WS.

### WS-Based Simulation Training

Perhaps wsv can serve as a simulation of the real world, and scene creation is convenient. If with 1 billion different scenes, we will have 1 billion non-artificial natural simulation scenes.

### Audio Processing in WS

We can set sound attenuation at different pixels through relative distance, like when an Agent explores in wsv files, the sound differs at each position. We have many audio aspects to explore in this format.

### WS-Based Database Development

Conversion from png to wsg, wsg extraction, usage and storage, compression. These are all directions that need development.

### Application of Gaussian Algorithms in WS

Although I believe current Gaussian algorithms might affect WSG file quality, if we don't have suitable mechanical devices to extract existing world information, we can use Gaussian as a recording substitute.
Moreover, the Gaussian field has great potential to apply related methods to our WS files.

### WS-Based Autonomous Driving

If a model trains on WSV files, it might learn to understand the existing world, like relative and absolute distances. If so, vision-based autonomous driving might be greatly enhanced because it has learned and stored radar distance knowledge.

### WS-Based Medical Image Processing

The human body itself has a three-dimensional structure, WSV might record all patient body information without needing to read frame by frame of body layers.

### Secure and Efficient WS Computing

Perhaps new architectures can perform faster WSG calculations.

### WS-Based Software Engineering

WS Vedio players need support across all platforms.

...

There are many more fields I know or don't know about, related researchers can all try.

*Conceived this blog on 23th Dec 2024 and completed on 23th Dec 2024*