<div align="center">
  <h1>Model & Paper</h1>
  <p><strong>Trending open-source machine learning models and research papers, updated daily.</strong></p>

<!-- COUNTERS:START -->
<p align="center">
  <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/papers/README.md"><img src="https://img.shields.io/badge/Papers-46%20Indexed-2563eb?style=flat-square" alt="Papers Count"></a>
  <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/models/README.md"><img src="https://img.shields.io/badge/Models-48%20Indexed-16a34a?style=flat-square" alt="Models Count"></a>
  <a href="https://axiomrepo.substack.com/"><img src="https://img.shields.io/badge/Newsletter-Axiom%20Repo-ff6719?style=flat-square&logo=substack" alt="Axiom Repo Newsletter"></a>
  <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-gray?style=flat-square" alt="License"></a>
</p>
<!-- COUNTERS:END -->

  <p>
    <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/models/README.md">Browse Models</a> ·
    <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/papers/README.md">Browse Papers</a> ·
    <a href="https://axiomrepo.substack.com/">Newsletter</a> ·
    <a href="https://github.com/BELYAGOUBIABDELILAH">GitHub Profile</a> ·
    <a href="mailto:belyagoubiabdillah@gmail.com">Contact</a>
  </p>
</div>

<hr>

<p>
  <strong>Model & Paper</strong> is an open-source index tracking trending machine learning models and research papers from Hugging Face. Each entry is stored as an individual Markdown brief, with repository indexes updated daily.
</p>

### Axiom Repo Newsletter

Weekly coverage of open-source AI models and machine learning research papers.

[Subscribe to Axiom Repo](https://axiomrepo.substack.com/)

---

## Latest Research Papers

<!-- PAPERS:START -->
* **[Mixture-of-Loops Transformer](./papers/2026-11-27-mixture-of-loops-transformer.md)** ([Source](https://huggingface.co/papers/2611.34923))  
  Looped Transformers boost expressivity by reusing shared layers across loops, yet at the cost of efficiency. Pushing their expressivity-efficiency frontier requires rethinking the core mechanism connecting adjacent loops: What should be passed as a Transformer loops? We introduce Mixture-of-Loops Transformer (MoLT), whose Mixture-of-Loops Attention (MoLA) uses keys and values (KV) as memory for selective reuse across depths and loops.

* **[Sage-Med: Scaling Medical Multimodal Intelligence](./papers/2026-11-26-sage-med-scaling-medical-multimodal-intelligence.md)** ([Source](https://huggingface.co/papers/2611.34575))  
  Establishing effective scaling laws for medical multimodal large language models (MLLMs) remains a persistent and fundamental challenge. Our systematic evaluation shows that existing medical MLLMs tend to underperform frontier general-purpose MLLMs across a range of medical tasks, while scaling model size primarily improves text capabilities rather than multimodal perception, and enabling reasoning modes fails to close this visual gap. To investigate how medical multimodal intelligence scales in practice, we int...

* **[Real2SimLab: A Unified Platform for Real-to-Simulation Transfer](./papers/2026-11-26-real2simlab-a-unified-platform-for-real-to-simulation-transf.md)** ([Source](https://huggingface.co/papers/2611.34849))  
  Real-to-simulation transfer, which builds simulations from real-world observations, has long been studied in research and industry. Recently, coding agents have become capable of generating simulation programs from video recordings, and several benchmarks have been proposed to evaluate them. However, each individual benchmark defines its own inputs, deliverables, and scoring pipeline.

* **[PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement](./papers/2026-11-25-partagent-agentic-3d-part-segmentation-via-expert-integratio.md)** ([Source](https://huggingface.co/papers/2611.32554))  
  Segmenting a 3D object into semantically meaningful parts requires joint reasoning about geometric structure and semantic context. Pretrained 3D experts provide spatially grounded region proposals, while 2D experts provide semantic cues for identifying object parts. The challenge is to integrate these complementary capabilities into a framework that can both produce meaningful part segmentations and progressively refine them.

* **[Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe](./papers/2026-11-25-lazy-agents-answer-against-their-own-beliefs-reinforcement-l.md)** ([Source](https://huggingface.co/papers/2611.32884))  
  AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode scores only the final answer, so it cannot teach the agent when to commit, because a lucky guess receives the same reward as an answer backed by evidence.
<!-- PAPERS:END -->

<p><a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/papers/README.md">View all <!-- PAPERS_COUNT -->46<!-- /PAPERS_COUNT --> research papers in archive →</a></p>

---

## Latest Open-Source Models

<!-- MODELS:START -->
* **[strata-engine/Inkling-2-Mini-Strata](./models/2026-11-27-inkling-2-mini-strata.md)** ([Source](https://huggingface.co/strata-engine/Inkling-2-Mini-Strata))  
  Inkling-2-Mini-Strata is a multimodal image and text understanding model from strata-engine. Inkling 2 Mini is Thinking Machines Lab's open-weights model made to run on local hardware. It is a looped transformer: the middle layers run three times for every token. It has 26.4B parameters and uses 3.4B per token (5.4B when the repeated passes are counted).

* **[ISTA-DASLab/Inkling-2-Mini-GSQ-RCO-GGUF](./models/2026-11-27-inkling-2-mini-gsq-rco-gguf.md)** ([Source](https://huggingface.co/ISTA-DASLab/Inkling-2-Mini-GSQ-RCO-GGUF))  
  Inkling-2-Mini-GSQ-RCO-GGUF is a text generation model from ISTA-DASLab. Each build is a single GGUF named after its quantization identifier: Inkling-2-Mini-GSQ-RCO- .gguf. The bpw is the average bit-width over the whole file, 26.07B parameters.

* **[nari-labs/Qwen3.8-27B-NariQ-GGUF](./models/2026-11-26-qwen3-8-27b-nariq-gguf.md)** ([Source](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF))  
  Qwen3.8-27B-NariQ-GGUF is a multimodal image and text understanding model from nari-labs. The sampling flags are the thinking-mode settings our scores used. -c 131072 fits a 24 GB GPU with little to spare;

* **[nvidia/Nemotron-Labs-Image-30B-A3B](./models/2026-11-26-nemotron-labs-image-30b-a3b.md)** ([Source](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B))  
  Nemotron-Labs-Image-30B-A3B is a text-to-image generation model from nvidia. documents, charts, and scientific figures. Its Pixel as Code interface

* **[prism-ml/Ternary-Bonsai-2.5-27B-GGUF](./models/2026-11-25-ternary-bonsai-2-5-27b-gguf.md)** ([Source](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF))  
  Ternary-Bonsai-2.5-27B-GGUF is a text generation model from prism-ml. Ternary Bonsai 2.5 27B is the agentic release of the Ternary Bonsai 27B line. It keeps the Qwen3.8-27B hybrid-attention architecture and the ternary weight format of Bonsai 2, so it is still 1.76 bits per weight and 5.93 GB, against 53.8 GB for the FP16 model. This release targets long-horizon, tool-driven work.
<!-- MODELS:END -->

<p><a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/models/README.md">View all <!-- MODELS_COUNT -->48<!-- /MODELS_COUNT --> open-source models in archive →</a></p>

---

## Archive Directories

- **[Research Papers Archive](https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/papers/README.md)** — Complete chronological directory of all indexed machine learning research papers.
- **[Open-Source Models Archive](https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/models/README.md)** — Complete chronological directory of all indexed open-weight models.

---

<div align="center">
  <p>
    Curated and maintained by <a href="https://github.com/BELYAGOUBIABDELILAH"><strong>Belyagoubi Mohammed Abdelilah</strong></a><br>
    <a href="https://axiomrepo.substack.com/">Newsletter</a> · <a href="https://github.com/BELYAGOUBIABDELILAH">GitHub Profile</a> · <a href="mailto:belyagoubiabdillah@gmail.com">Contact</a>
  </p>
</div>
