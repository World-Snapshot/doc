# Q&As

## How to Contribute?

For us, generally speaking, our work is to make things as componentized as possible: 

1. It is structured with fixed interfaces, for example, the main model of WaveGen is located in a certain folder in the repository, and all the other files are calls to it. This enables us to switch model architectures simply by changing the folder. 
2. ControlWave also calls files in a certain folder or folders under plugins. They have their own independent tabs. This means that all the plugins, all the model decoders, they should all be independent and isolated from each other. Installing plugins/models, uninstalling plugins/models should only involve adding or removing folders in specific locations. 

The advantage of this approach is that everyone can edit and upgrade in their own warehouse. And even there is no need to submit a PR. As long as their work can be called by ControlWave, anyone just needs to open the panel, then manually put a certain folder in, or provide a download link when using it, and then they can use a certain plugin or model. 

This kind of thinking has learned some game development thinking such as that of Minecraft and Terraria mods. This enables everyone to easily make any improvements to our work, while we only provide a UI platform for maintenance. It is very important to give any developer sufficient permissions without affecting the core game itself.

We also welcome contributions in all forms:

- Try to add new changes or functions instead of modifying the existing code.
- Try to discuss in Github rather than elsewhere.
- We will try to install an automatic test for the main functions before release. As long as your changes do not affect the main functions, we will consider adding them at our discretion. Of course, it is recommended to use compatible plugins: simply place your plugin in our plugin folder or download it through a link to the plugin folder for use. This method is the best.
- We estimate that in the majority of future PR cases, it will be debugging of ControlWave. Of course, we have other projects and these projects may have different situations. We will update this document in a timely manner when the time comes.

Please check the respective repositories on how to contribute, if has addtional intro. :)

## Future Work

Here, we take stock of the things that can be done in the future.

1. First of all, at the beginning of this project, we had a [brief reflection](https://world-snapshot.github.io/doc/index.html?page=S5_blogs/02_cv_rebirth.md).

2. We can explore more generation methods to create the core space: perhaps 4D CNN is a better foundation for the world model and a way to construct the core space; perhaps RNN like RWKV, Mamba, which are naturally suitable for maintaining states and align with our explicit world state concept; perhaps the super-large Gaussian volume can replace the wave space; perhaps the traditional several image generation methods (e.g., 3D VAE to TSDF to Mesh) can be changed into a two-stage method to create the core space...