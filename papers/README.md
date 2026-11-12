# Research Papers Archive

Total indexed: **17** papers.

[← Back to Model & Paper](https://github.com/BELYAGOUBIABDELILAH/model-and-paper)

---

* **[Few-Step Streaming Video Generation via Condition Shifting](./2026-11-12-few-step-streaming-video-generation-via-condition-shifting.md)** ([Source](https://huggingface.co/papers/2611.14033))  
  Few-step sampling reduces the cost of streaming video generation. Distribution Matching Distillation (DMD) supervises few-step generators with a separate fake-score network, which adds training memory and computation and must track the evolving generator. We extend APEX to streaming video by using condition shifting to estimate the velocity field of the generated distribution within the generator.

* **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](./2026-11-11-tree-ising-repairing-language-models-with-bit-level-ising-ed.md)** ([Source](https://huggingface.co/papers/2611.14210))  
  Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-pass requests. Our method, Tree-Ising, casts this repair as a sparse discrete optimization problem over the model's own BF16 weights.

* **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](./2026-11-11-don-t-just-trust-your-memory-evidence-linked-memory-reduces.md)** ([Source](https://huggingface.co/papers/2611.14320))  
  External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled only with task success or failure, yet are typically provided without the trajectories they came from...

* **[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](./2026-11-10-learning-heterogeneous-tactile-representation-for-general-de.md)** ([Source](https://huggingface.co/papers/2611.12806))  
  Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering irreplaceable strengths alongside its own drawbacks. A key challenge is thus to free tactile understanding from sensor-specific physics, so that embodied models can effectively leverage heterogeneous tactile data.

* **[Video-Coder: Reinforcing Agentic Coding for Video Generation](./2026-11-09-video-coder-reinforcing-agentic-coding-for-video-generation.md)** ([Source](https://huggingface.co/papers/2611.09894))  
  Recent years have witnessed remarkable progress in video generation in terms of visual quality and temporal consistency. However, generating videos with precise spatial structure, coherent motion dynamics, and controllable scene composition remains challenging. In this paper, we introduce Video-Coder, the first attempt to train a code-driven video generation agent, which autonomously writes and executes code to construct a dynamic 3D scene (Draft Video) that provides structure and motion signals to downstream vi...

* **[SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes](./2026-11-09-splatanything-gaussian-spacing-normalization-for-feed-forwar.md)** ([Source](https://huggingface.co/papers/2611.08264))  
  We identify a key limitation of existing feed-forward 3DGS methods: Gaussian attributes are typically predicted in a radial-distance-normalized space that canonicalizes a global radial statistic of the reconstructed geometry, while the spacing between neighboring Gaussian centers can still vary substantially across scene scales and camera configurations. This mismatch induces systematic shifts in Gaussian-scale targets, leading to ambiguous supervision. To address this, we propose SplatAnything with Gaussian Spa...

* **[Towards Foundation Decision Models: Drex](./2026-11-08-towards-foundation-decision-models-drex.md)** ([Source](https://huggingface.co/papers/2611.07854))  
  Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of outputs, and add cost and latency. Decision models address this: given a question and a set of options supplied by the user, they return a probability distribution over the options without autoregressive decoding.

* **[EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure](./2026-11-08-edgar-efficient-diffusion-driven-gaussian-avatar-refinement.md)** ([Source](https://huggingface.co/papers/2611.07909))  
  Recent advances in Gaussian splatting have enabled efficient and photorealistic head avatar reconstruction, yet monocular video-based or image-based methods still suffer from under-constrained geometry and texture, leading to artifacts such as blurring, stretching, and temporal instability. We present EDGAR (Efficient Diffusion-Driven Gaussian Avatar Refinement), a conditional diffusion framework designed to enhance the quality of Gaussian avatars by correcting artifacts while preserving identity fidelity. To tr...

* **[WeLM-Image: A Unified Image Generation Model towards Visual Intelligence](./2026-11-07-welm-image-a-unified-image-generation-model-towards-visual-i.md)** ([Source](https://huggingface.co/papers/2611.07392))  
  We present WeLM-Image, a unified image foundation model that integrates multimodal understanding into text-to-image generation, instruction-guided editing, and multi-reference synthesis. Designed for single-GPU deployment in WeChat's large-scale consumer applications, the model processes text, reference images, and target latents as one interleaved sequence. A Mixture-of-Transformers (MoT) backbone combines shared attention with independent understanding and generation parameters to limit optimization interference.

* **[The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks](./2026-11-07-the-last-mile-to-the-real-world-agent-native-primitives-as-r.md)** ([Source](https://huggingface.co/papers/2611.07461))  
  How can an agent handle a real-world task end to end? Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% of the tasks and Claude Opus 5 with Claude Code 51.8%. These tasks fail at the step from reaching a resource to applying it, which we call the last mile to the real world.

* **[VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding](./2026-11-06-vflash-fast-accurate-visual-planning-via-flash-primitive-dec.md)** ([Source](https://huggingface.co/papers/2611.08449))  
  Models for physical AI tasks, such as robotics and autonomous driving, need not reason solely in language. They can use visual plans--points, bounding boxes, and trajectories--to represent spatial goals and anticipate motion. However, autoregressive vision-language models generate these plans one coordinate token at a time, making richer predictions increasingly costly.

* **[SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](./2026-11-06-sla-scaling-spatial-language-action-model-via-continual-pre.md)** ([Source](https://huggingface.co/papers/2611.08373))  
  Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience.

* **[Turns Matter: Advancing Streaming Video RL via Turn-Level Credit](./2026-11-05-turns-matter-advancing-streaming-video-rl-via-turn-level-cre.md)** ([Source](https://huggingface.co/papers/2611.06728))  
  Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied to this setting, with existing approaches emphasizing reward design while retaining a single trajectory-level advantage across turns. Such shared credit can reinforce redundant replies after earlier successes and discourage useful follow-ups after earlier failures.

* **[REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control](./2026-11-05-rea-routed-embodied-agent-runtime.md)** ([Source](https://huggingface.co/papers/rea-routed-embodied-agent))  
  Foundation models are becoming remarkably reliable at high-level reasoning, yet they remain too slow and costly to serve as fine-grained controllers. Conversely, fast policies like VLAs and whole-body controllers offer more efficient reflexes, but struggle to generalize.

* **[FrontierPhysics: Evaluating Agents for End-to-End Physics Research](./2026-11-05-frontierphysics-evaluating-agents-for-end-to-end-physics-res.md)** ([Source](https://huggingface.co/papers/2611.06910))  
  AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-to-end benchmark with 56 tasks made by 42 physicists based on their own research, covering nine domains across theoretical, computational, and experimental physics.

* **[From Pixels to Actions - Towards Native Vision-Language-Action Policies](./2026-11-05-from-pixels-to-actions-towards-native-vision-language-action.md)** ([Source](https://huggingface.co/papers/2611.06918))  
  Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation?

* **[Agentic Reasoning in Autonomous Large Language Models](./2026-11-03-agentic-reasoning-autonomous-llms.md)** ([Source](https://huggingface.co/papers/agentic-reasoning-autonomous-llms))  
  A unified framework for multi-step planning, tool execution, and self-correction in autonomous LLM agents operating across long-horizon software engineering tasks.

---

Curated by [Belyagoubi Mohammed Abdelilah](https://github.com/BELYAGOUBIABDELILAH) · [Contact](mailto:belyagoubiabdillah@gmail.com) · [Newsletter](https://axiomrepo.substack.com/)
