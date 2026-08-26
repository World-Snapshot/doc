# Computer Vision’s Rebirth

<!--*“The best research is like water, which nourishes all things without contention.”*-->


For more than half a century, computer vision has grown by dividing visual intelligence into separate tasks: classification, localization, detection, segmentation, estimation, reconstruction, tracking, generation, editing, rendering, planning, and control. Each task acquired its own data format, architecture, objective, benchmark, and deployment stack. This specialization created a vast field, but it also fragmented the field.

The Unified Law for Visual Tasks suggests another direction. If visual information can be encoded at the image boundary, then a visual task can be expressed as a generative transformation from available evidence to a requested World Snapshot target. **World Snapshot Graphics (WSG)** supplies the shared representation; **World Snapshot Models (WSMs)** learn the transformations; **TunnelingNet Channel Heads** make task routes trainable, selectable, repairable, and extensible.

Computer vision can therefore grow like a language model rather than like a directory of unrelated programs. A new aligned modality does not create only one capability. It becomes a new node in the Tree of Computer Vision and immediately forms families of estimation, generation, control, reconstruction, and multi-condition tasks with the existing nodes. Longer routes form Chains of Visual Thought. Sparse interfaces allow structured, symbolic, audio, sensor, and agent information to participate without being forcibly expanded into a dense image tensor.

This is what I mean by the **rebirth of computer vision**: the field changes from individually engineering visual tasks to generating, composing, training, routing, and deploying visual capabilities inside one expandable system.

### Universal Computer Vision

General computer vision, visual and multimodal foundation models, world models, World Snapshot Models, visual and multimodal agents, embodied intelligence, physical intelligence, spatial intelligence, and world reasoning can share one task language.

Within this language, classification, localization, detection, segmentation, estimation, reconstruction, restoration, completion, registration, correspondence, tracking, retrieval, indexing, prediction, generation, editing, rendering, simulation, planning, and control become requested visual outputs rather than isolated model species. The same system can support any-input-to-any-output vision, multi-input single-output and multi-input multi-output routes, multi-condition and multi-target generation, and unified, continual, incremental, modular, compositional, and open-world visual learning.

This also creates the basis for automatic visual-task discovery and generation, task and model routing, tool and expert routing, visual-capability composition, workflow generation, optimization, execution, and verification.

### Visual Reasoning and Chains of Visual Thought

A visual task graph is also a reasoning graph. A route can move from RGB to depth, from depth to normals, from normals and a reference frame to RGB, or through a longer sequence of geometric, physical, material, semantic, temporal, and sparse variables. Every intermediate result remains inspectable and machine-usable.

This supports visual reasoning, Chains of Visual Thought, compositional and large-scale visual reasoning, multimodal and cross-modal reasoning, physical, spatial, temporal, causal, counterfactual, and common-sense reasoning, and interactive world reasoning. Breadth comes from adding modalities and directed routes; depth comes from composing those routes into longer visual programs.

### Computer Graphics in World Snapshots

WSG extends the pixel from a color carrier into a world-snapshot atom. RGB remains important, but geometry, motion, pose, segmentation, materials, physical properties, audio associations, confidence, and structured observations can occupy aligned variables at the same boundary.

This creates a computer-graphics research program around World Snapshots: encoding, rendering, visualization, compression, storage, transmission, interpolation, extraction, injection, conversion, validation, and editing of WSG and WSV; developing line, lighting, shape, surface, motion, and material representations; and studying how dense and sparse variables should interact.

The result is not merely a richer image file. It is a common computational surface on which graphics, vision, generation, perception, and reasoning can meet.

### Generative Visual Perception and Understanding

Perception does not have to end in a private feature vector or a task-specific scalar head. A model can generate the requested depth map, normal field, skeleton, segmentation, physical-property map, material map, object identity, or structured observation in an explicit representation.

This turns visual perception and understanding into generative visual tasks. It also makes intermediate evidence easier to inspect, compose, correct, cache, share, and reuse. Classification or categorical masks may use a task-integrated categorical refiner, while the spatial region remains generated by the task route itself.

### Classification, Localization, Detection, and Segmentation

The same framework can cover image, video, object, scene, material, action, behavior, event, sound, and cross-modal classification; open-vocabulary, fine-grained, zero-shot, and few-shot classification; object, keypoint, text-guided, visual-language, sound-source, 3D, and spatiotemporal localization; and 2D, 3D, video, small-object, dense, occluded, anomaly, defect, event, action, audio-instance, and multisensor detection.

Segmentation extends across semantic, instance, panoptic, part, human, object, video, 3D, 4D, interactive, open-vocabulary, audio-instance, material, motion, scene, medical, remote-sensing, industrial-defect, affordance, contact-region, and risk-region targets.

These tasks differ in evidence and requested output, but their visual interfaces are compatible. Dense masks can express spatial support; sparse adapters can express boxes, points, identities, sets, relations, and variable-length structures.

### Geometry, Motion, Pose, and Structure

World Snapshot variables naturally support monocular, stereo, video, metric, and relative depth; disparity; surface normals; curvature; edges and contours; optical flow and scene flow; motion; camera and object pose; 2D and 3D human pose; hand and face pose; skeletons; human parameters; object and scene structure; scale, distance, speed, acceleration, trajectory, deformation, articulation, occlusion, and visibility.

These variables can be estimated from RGB, generated as controls for RGB, translated into one another, reconstructed from multiple observations, or composed into longer geometric reasoning routes. Geometry is therefore not a single auxiliary prediction. It is a connected domain inside the task graph.

### Layered Human Motion Synthesis

When a World Snapshot Model generates a human, it can generate several aligned layers: RGB appearance, human segmentation, surface normals, depth, parametric 3D body structure, and 2D or 3D skeletons. These layers correspond at the image boundary and can constrain one another.

The useful intuition is shadow puppetry with many synchronized layers. A sideways palm should not merely resemble a hand in RGB; its fingers, silhouette, depth, normals, skeleton, and body structure should remain mutually plausible. This supports pose estimation, motion analysis, motion transfer, animation, rehabilitation assessment, sports analysis, action scoring, sign-language recognition and generation, virtual humans, digital actors, motion capture, expression capture, face reenactment, lip synchronization, and audio-driven animation.

### Occlusion, Visibility, and the World Snapshot Clothing Paradox

An RGB image exposes only the visible surface. A richer World Snapshot may separately represent instance identity, segmentation, depth, visibility, and other layered evidence. This gives a model more structure for reasoning about overlapping objects and reduces the chance that one entity simply disappears behind another.

The hidden appearance itself remains uncertain. If the visible sleeve of an occluded person is red, a model may infer that the hidden clothing is red, but the torso may in fact be blue. The representation should preserve the known geometry and visibility while allowing the generative model to resolve the unobserved appearance. I call this the **World Snapshot Clothing Paradox**: the hidden region is structurally constrained but visually underdetermined.

### Physical and Material Intelligence

World Snapshots can encode and predict lighting, reflectance, albedo, texture, shadow, transparency, roughness, metalness, refractive index, density, mass, volume, relative weight, support area, friction, elasticity, stiffness, hardness, temperature, pressure, stress, strain, flow, contact state, collision risk, affordance, stability, load-bearing capacity, uncertainty, confidence, risk, and reward.

This is a bridge from appearance recognition to physical and material reasoning. A model can estimate a property from RGB, use that property to control generation, infer one property from another when the evidence is sufficient, or combine several weak observations. It supports physical-property estimation, material characterization and discovery, contact and affordance reasoning, safety analysis, manipulation, simulation initialization, and scientific measurement.

### Pixel-Level Editing and Transfer

Aligned variables make editing more explicit. If two WSV clips contain different people performing related motions, RGB appearance may be transferred while pose, segmentation, depth, normals, or motion variables remain fixed. Conversely, pose or motion may change while identity and appearance are retained.

The same principle extends to image, video, 3D, 4D, scene, object, character, material, lighting, motion, camera, pose, expression, clothing, background, local-region, semantic, and physical-property editing. It also covers colorization, style transfer, domain transfer, image-to-image and video-to-video translation, reference-guided generation, and consistency across characters, objects, scenes, views, shots, time, geometry, physics, materials, lighting, motion, and audio.

### Generation, Restoration, and Completion

A unified generative interface can serve general image and video generation, long and real-time video, interactive video, multiview image and video, 3D and 4D content, spatial video, immersive content, controllable generation, and reference-image generation.

The same target-oriented formulation also covers generative restoration: image, video, and 3D repair; old-photo and cultural-heritage restoration; denoising; deblurring; super-resolution; image, video, scene, object, occlusion, and missing-modality completion; colorization; and sim-to-real or real-to-simulation translation.

Text-to-image, text-to-video, text-to-3D, image-to-3D, video-to-3D, 3D-to-image, 3D-to-video, audio-to-image, audio-to-video, image-to-audio, and video-to-audio can be understood as routes connecting different evidence spaces to requested targets.

### Reconstruction and Inverse Rendering

Reconstruction includes image, video, 3D, 4D, multiview, dynamic-scene, human, hand, face, object, indoor, outdoor, city, building, road, terrain, underwater, and underground reconstruction. It also includes medical and scientific imaging, NeRF and Gaussian-splatting reconstruction, point clouds, meshes, voxels, occupancy fields, materials, lighting, sound fields, physical fields, RGB-D, and multi-attribute generative reconstruction.

RGB-assisted inverse rendering is especially important: a partial observation supplies evidence about the requested property, while RGB provides identity, layout, texture, and context that the partial observation does not contain. This practical interface turns many otherwise ambiguous cross-variable mappings into usable reconstruction routes.

### World Generation, Memory, and Digital Twins

Changing the target from RGB to a World Snapshot changes image generation into world-snapshot generation. The output can carry many aligned properties rather than only visible color. Extending the sequence produces World Snapshot Video; extending representation and memory supports persistent, dynamic, interactive, generative, predictive, physical, robotic, autonomous-driving, game, cinematic, and embodied world models.

This supports past-snapshot reconstruction, hidden-variable inference, snapshot updating, repair, branching, rollback, retrieval, querying, completion, fusion, compression, transmission, databases, search engines, knowledge bases, and digital assets. It also supports real-time and generative digital twins for industry, cities, people, vehicles, robots, buildings, Earth systems, environments, and medicine.

### World Snapshot Data and Data Mining

Early WSG data can be assembled from existing perception models, renderers, simulators, structured datasets, and manual annotations. Higher-quality mechanical and multimodal sensors can record the same variables more directly. The format makes the origin, normalization, visualization, extraction, and confidence of every variable part of the data contract.

Training a text-to-WSG model is not merely training text-to-image with extra decoration. It creates outputs with many analyzable variables. A World Snapshot may be indexed or classified through pose, motion, depth, sound, material, geometry, identity, and physical properties rather than through a single label.

The same infrastructure supports synthetic-data generation, augmentation, automatic annotation, pseudo-label generation, training and evaluation data generation, benchmark generation, long-tail and rare-event generation, safety testing, counterfactual data, model evaluation, diagnosis, interpretability, uncertainty analysis, and geometric, physical, semantic, temporal, cross-view, and cross-modal consistency verification.

### Audio, Sensors, and Multimodal Fusion

Audio can identify active sources, condition visual generation, associate a sound with one or several spatial regions, or complement RGB and geometric evidence. Relative distance and scene structure can further support spatial sound, attenuation, sound-field reconstruction, and audio-visual reasoning.

The same sparse and dense interfaces can incorporate radar, LiDAR, touch, inertial sensing, multispectral and hyperspectral imagery, thermal imaging, event cameras, medical sensors, and other measurements. This enables sensor fusion, cross-sensor generation, missing-sensor completion, calibration, simulation, and audio-visual, radar-visual, LiDAR-visual, tactile-visual, inertial-visual, spectral, thermal, and event-camera fusion.

### Visual Agents and Embodied Intelligence

A visual agent can use the task graph as a capability space. It can select an edge, request a depth map or physical property, compose several edges into a visual workflow, inspect intermediate World Snapshots, verify consistency, and revise the route.

This supports multimodal and embodied agents; perception, planning, control, navigation, manipulation, grasping, avoidance, mapping, exploration, imitation learning, reinforcement learning, skill learning and composition, fault diagnosis, safety control, human-robot collaboration, and multisensor fusion. It also supports visual-language-action models, multi-agent collaboration, distributed world models, shared World Snapshots, and cloud-edge visual intelligence.

### Robotics and Autonomous Systems

Robotics applications include household, service, industrial, medical, surgical, rehabilitation, logistics, warehouse, agricultural, underwater, aerial, space, biomimetic, and general-purpose robots.

Autonomous-driving applications include vehicle perception, localization, planning, and control; lane and drivable-area detection; traffic-participant detection; scene and trajectory prediction; collision prediction; risk assessment; driver behavior and monitoring; parking; vehicle-road cooperation; intelligent transportation; traffic simulation and digital twins; data generation; scene reconstruction; and counterfactual safety testing.

Drone and unmanned-system applications include navigation, inspection, surveying, obstacle avoidance, formation, tracking, mapping, environmental perception, search and rescue, and collaborative autonomy.

### Scientific Computing and Simulation

World Snapshots can connect observations to simulators and physical fields. Relevant directions include fluid, structural, thermodynamic, electromagnetic, acoustic, particle, and molecular simulation; physics-informed learning; experimental analysis and design; materials discovery; microscopy; telescope and planetary imagery; Earth observation; and scientific discovery.

A generative model can create diverse simulation initializations, infer missing physical variables, reconstruct fields from partial observations, or translate between measurements and visualizable results. Gaussian representations, radiance fields, meshes, point clouds, voxels, occupancy fields, and other scene representations can participate as source data, targets, or external tools without replacing the World Snapshot interface.

### Medicine and Life Sciences

Medical applications include clinical decision support, lesion detection, tumor and organ segmentation, anatomical reconstruction, surgical planning and navigation, radiotherapy planning, longitudinal imaging, pathology, digital pathology, cell segmentation and tracking, tissue analysis, disease progression, biomechanics, movement analysis, rehabilitation, vital-sign estimation, telemedicine, and medical digital twins.

Scientific imaging includes MRI, CT, ultrasound, microscopy, pathology, protein imaging, and other inverse problems. Agricultural and ecological applications include crop monitoring, pests and disease, weeds, fruit counting, maturity and yield, soil conditions, precision agriculture, livestock, aquaculture, forestry, and marine ecology.

### Earth, Environment, and Infrastructure

Remote-sensing and geospatial applications include aerial and satellite analysis, land-cover classification, land use, geospatial reasoning, map generation and updating, 3D and high-definition maps, indoor and navigation maps, GIS, weather and climate imagery, and environmental change detection.

Monitoring extends to floods, fires, earthquakes, landslides, glaciers, coastlines, forests, water, oceans, ships, ports, roads, bridges, tunnels, railways, airports, power grids, pipelines, water systems, communication infrastructure, buildings, construction quality, and energy use. These capabilities support disaster response, damage assessment, reconstruction, resource allocation, smart cities, city planning, and city operations.

### Industry, Commerce, and Everyday Systems

Industrial vision includes manufacturing, quality inspection, surface defects, dimensions, assembly, welding, part recognition and pose, process monitoring, equipment status, predictive maintenance, fault localization and reasoning, process optimization, production-line digital twins, logistics, sorting, inventory, shelves, package inspection, traceability, and materials analysis.

Commercial applications include retail vision, product recognition and retrieval, visual search, inventory, cashierless stores, virtual try-on, clothing and product generation, advertising, recommendation, brand assets, marketing, media production, insurance assessment, real-estate visualization, virtual tours, interior design, spatial layout, and furniture placement.

Everyday systems include smart homes, household understanding and digital twins, appliance control, energy management, indoor safety, care for older adults and children, pet monitoring, smart glasses, wearables, mobile vision, edge vision, and visual IoT.

### Media, Games, and Spatial Computing

Media applications include AI film, television, animation, short video, advertising, live streaming, virtual production, previs, shot planning, storyboards, digital actors, virtual humans, visual effects, post-production, editing, summarization, retrieval, understanding, question answering, and media-asset management.

Games can use World Snapshots for world, level, character, animation, material, physics, and scene generation; scene reconstruction; game agents and non-player characters; interactive narrative; persistent and open worlds; content updates; and mod ecosystems. A World Snapshot contains more machine-usable structure than an RGB frame, so an agent may inspect distance, motion, pose, sound association, segmentation, and physical attributes while it explores.

Spatial computing includes virtual, augmented, and mixed reality; immersive training; virtual laboratories and museums; digital exhibitions; cultural-heritage digitization; archaeological reconstruction; design; education; professional training; driving, flight, medical, military, and emergency simulation.

### Accessibility, Safety, and Public Services

Accessibility applications include blind and low-vision navigation, visual question answering assistance, image and video description, accessible-content generation, captions, sign-language recognition, generation, and translation, and sound-scene understanding.

Safety applications include anomaly behavior, people and crowd analysis, tracking, abandoned objects, intrusion, campus, airport, industrial and construction safety, fire and smoke warnings, hazardous materials, identity verification, face and gait recognition, liveness, forensics, authenticity and deepfake detection, provenance, copyright, and privacy-preserving vision.

The same task families support emergency command, disaster response, search and rescue, accident reconstruction, evidence analysis, terrain understanding, equipment monitoring, reconnaissance, and coordinated unmanned systems.

### A Visual Capability Ecosystem

When a capability is represented as a directed task route, it can be trained and deployed as a module without becoming an isolated product. This supports capability hot loading, hot updates, hot swapping, incremental deployment, versioning, rollback, diagnosis, repair, validation, compatibility testing, authorization, metering, and service delivery.

It also supports visual-task routing, model routing, tool routing, expert routing, capability orchestration, workflow generation and optimization, model and capability fusion, distillation, merging, compression, cloud service, edge and private deployment, multi-tenant service, capability markets, plugin ecosystems, and visual-task or multimodal-capability services.

ControlWorld is one early interface for this idea: select a trained route in the Tree of Computer Vision, provide the required evidence, and generate the requested target. In the longer term, a visual agent should be able to select, compose, test, and repair these routes automatically.

### From a Field of Tasks to a Task-Generative Field

The most important consequence is not any single application above. It is the rate at which applications become expressible. Adding one aligned modality creates many new directed tasks with the existing modalities. Adding sparse variables introduces structured tasks. Composing routes increases reasoning depth. Improving one shared representation or generator can benefit many routes at once, while a weak route can still be repaired independently.

Computer vision may therefore move beyond a fixed catalog of named tasks. Like large language models, which support an effectively unbounded number of language uses without assigning a separate model identity to every prompt, World Snapshot Models can gradually absorb increasingly fine-grained visual tasks into one expandable generative system.

The inventory above deliberately mixes two different levels: **visual task definitions** and **application scenarios**. It is neither a count of WSM tasks nor a limit on possible deployments. A task is defined by its available evidence and requested target; the same task can serve many application scenarios, while one application may compose many tasks, tools, and reasoning routes. Therefore, the number of visual tasks expressible by WSM exceeds the number named here, and the number of possible application scenarios is much larger still.

The list is not a promise that every application has already been completed. It is a research map showing which visual, physical, multimodal, embodied, scientific, industrial, and creative problems can be expressed through World Snapshot representations and WSM task interfaces. Many directions already exist as computer-vision fields; many become newly composable under WSM; others become new tasks when their input evidence or requested output changes.

There are many more fields I know or do not yet know. Researchers from each field can add the variables, data, routes, tools, and evaluations that their problems require. That is how computer vision can be unified, expanded, and ultimately reborn.

*Conceived this blog on 23 December 2024; substantially updated for WSM v1 Augustus on 26 August 2026.*
