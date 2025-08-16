# Q&As

You can consider this page as a super navigation page. The Github organization itself already has a [simple navigation page](https://github.com/World-Snapshot), but this one is much more detailed.

## How to Contribute?

Overall, It is like Minecraft or Terraria - it is forward-compatible/game-mod-style. We strive to make it easy for everyone to contribute, even without submitting a PR. Of course, we also fully welcome submissions. 

<details>
<summary>How do we conceive of modular contributions:</summary>

1. It is structured with fixed interfaces, for example, the main model of WaveGen is located in a certain folder in the repository, and all the other files are calls to it. This enables us to switch model architectures simply by changing the folder. 
2. ControlWave also calls files in a certain folder or folders under plugins. They have their own independent tabs. This means that all the plugins, all the model decoders, they should all be independent and isolated from each other. Installing plugins/models, uninstalling plugins/models should only involve adding or removing folders in specific locations.
3. For the backend of ControlWave, we mainly place the newly added functions in this backend/python file under this plugin folder. If some basic functions are needed, we will call this backend located in the root directory. This way, we can ensure the modularization of the plugin. Unless you think certain functions are necessary and other plugins might also use them, after discussing with us, you can update them to this backend in the root directory.

The advantage of this approach is that everyone can edit and upgrade in their own warehouse. And even there is no need to submit a PR. As long as their work can be called by ControlWave, anyone just needs to open the panel, then manually put a certain folder in, or provide a download link when using it, and then they can use a certain plugin or model. 

This kind of thinking has learned some game development thinking such as that of Minecraft and Terraria mods. This enables everyone to easily make any improvements to our work, while we only provide a UI platform for maintenance. It is very important to give any developer sufficient permissions without affecting the core game itself.

</details>

Each repository has a Contributing.md file that automatically displays on the code page of the repository, providing more details and the RoadMap of the repository:

- [Contribute to WaveGen](https://github.com/World-Snapshot/WaveGen?tab=contributing-ov-file)
- [Contribute to ControlWave](https://github.com/World-Snapshot/ControlWave?tab=contributing-ov-file)

We also welcome contributions in all forms:

- Try to add new changes or functions instead of modifying the existing code.
- Try to discuss in Github rather than elsewhere.
- We will try to install an automatic test for the main functions before release. As long as your changes do not affect the main functions, we will consider adding them at our discretion. Of course, it is recommended to use compatible plugins: simply place your plugin in our plugin folder or download it through a link to the plugin folder for use. This method is the best.
- We estimate that in the majority of future PR cases, it will be debugging of ControlWave. Of course, we have other projects and these projects may have different situations. We will update this document in a timely manner when the time comes.

## Future Work / Full RoadMap

Here, we take stock of the things that can be done in the future (Written on 16 August 2025, when the project is not yet mature enough to public).

Currently, wave generation models obtain the world representation of waves from the real world (Normalized depth map; or point cloud), (i.e., some kind of dynamic function or probability space wave). Due to the limitations of GPUs, wave models should only be able to demonstrate potential and are far from being mature. However, the world snapshot part, with the help of the mature ecosystem of RF, should be relatively better. 

I'm not saying that the wave generation model and the world snapshot are different parts. They are essentially the same thing. They need to be utilized together and form a whole. The wave generation model requires a wsg decoder. The world snapshot model also needs a core space. What I just mentioned was their bias. The world snapshot model is a model trained using the wave generation method. Although they are responsible for two orthogonal tasks, they still need to rely on each other. Perhaps only in a few cases do they need to be separate<sup class="footnote" data-note="(1) reconstruction, time-space, order and existence; (2) generation, rendering, understanding and cognition. Only when you focus on one of the two types of tasks will you propose WaveXyy or XyyWSM.">1</sup>. 

Therefore, we should:

### Phase One: 

- **Create sufficient datasets:** 1. For example, develop and use the SQ-SLAM method to convert the entire world into a wave function. 2. Perhaps the entire SMPL/MeshObj/Avatar ecosystems can be transferred over. 3. Integrate the SAM-Grounded tool with the existing wsg tools to obtain a better wsg dataset.

- **Improving and upgrading the wave2pixel:** I'm not sure if the model released for the first time can achieve a unified level of over 1500 visual tasks, but it is undoubtedly necessary to continue making improvements.

- **We can explore more generation methods to create the core space:** 1. perhaps 4D CNN is a better foundation for the world model and a way to construct the core space; 2. perhaps RNN like RWKV, Mamba, which are naturally suitable for maintaining states and align with our explicit world state concept; 3. perhaps the super-large Gaussian volume can replace the wave space; 4. perhaps the traditional several image generation methods (e.g., 3D VAE to TSDF to Mesh) can be changed into a two-stage method to create the core space...

- **Continue to increase the duration of the wave space:** By August 2025, it is impossible to achieve this in one step. We have to lower our goals. Perhaps the extremely long generation time or certain target concepts cannot be verified. We need to continuously prove the feasibility of the concepts.

### Phase Two:

- **Using sufficient data and GPU to train a complete model:** The new WSMs should be able to more comprehensively process the entire world, run a world more perfectly, quickly generate, understand, recognize, and reconstruct for visual and other tasks. And the version released in 2025 should only be a proof-of-concept version.

### Phase N: 

- Of course, at the beginning of this project, we had a [brief reflection](https://world-snapshot.github.io/doc/index.html?page=S5_blogs/02_cv_rebirth.md).

## How to cooperate?

For academic collaborations and any discussions, please send [emails](mailto:sen.fang@rutgers.edu)/[X(twitter)](https://x.com/SenFang01)/[Thread](https://www.threads.com/@senfang01) to the first author or the organization email. For more in-depth or business or funding collaborations, please send proposals, plans, and general details to [DM](mailto:dnm@cs.rutgers.edu) and copy the first author.