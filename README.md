<div align="center">
  <h1>Model & Paper</h1>
  <p><strong>Trending open-source machine learning models and research papers, updated daily.</strong></p>

<!-- COUNTERS:START -->
<p align="center">
  <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/papers/README.md"><img src="https://img.shields.io/badge/Papers-23%20Indexed-2563eb?style=flat-square" alt="Papers Count"></a>
  <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/models/README.md"><img src="https://img.shields.io/badge/Models-24%20Indexed-16a34a?style=flat-square" alt="Models Count"></a>
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
* **[TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models](./papers/2026-11-15-ttb-test-time-baking-for-efficient-rendering-of-decoder-only.md)** ([Source](https://huggingface.co/papers/2611.17331))  
  Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking (TTB), a strategy that learns to bake global scene information from cross-view attention into a lightweight MLP, enabling fast and high-fidelity novel-view decoding. The first key is to repurpose the fast-weight MLP o...

* **[Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors](./papers/2026-11-14-ropedia-xperience-2-a-gold-standard-for-scaling-physical-ai.md)** ([Source](https://huggingface.co/papers/2611.17060))  
  Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks in real-world environments. Further progress depends on two complementary resources: demonstrations of human behavior that supervise how tasks are performed, and interactive environments in which policies can be rolled out, evaluated, and improved in closed loop.

* **[Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](./papers/2026-11-14-actor-judge-or-teacher-understanding-decision-models-in-long.md)** ([Source](https://huggingface.co/papers/2611.17167))  
  Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach well.

* **[SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models](./papers/2026-11-13-so-arena-benchmarking-the-capability-spectrum-and-reliabilit.md)** ([Source](https://huggingface.co/papers/2611.15777))  
  System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited insight into the breadth of model capabilities and the reliability of their decisions.

* **[PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](./papers/2026-11-13-physloop-harnessing-llms-physics-awareness-for-self-improvin.md)** ([Source](https://huggingface.co/papers/2611.16748))  
  Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are difficult to obtain. Large language models (LLMs) possess physical knowledge, but struggle to reliably guide video generation models in producing their training videos.
<!-- PAPERS:END -->

<p><a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/papers/README.md">View all <!-- PAPERS_COUNT -->23<!-- /PAPERS_COUNT --> research papers in archive →</a></p>

---

## Latest Open-Source Models

<!-- MODELS:START -->
* **[Edge0/Edge0-145B-NVFP4](./models/2026-11-15-edge0-145b-nvfp4.md)** ([Source](https://huggingface.co/Edge0/Edge0-145B-NVFP4))  
  Edge0-145B-NVFP4 is a text generation model from Edge0. variables in env, with paths relative to the pack directory. That is the same file the Edge0 Chat app

* **[tencent/Qwen3.8-27B-DSpine-b16](./models/2026-11-14-qwen3-8-27b-dspine-b16.md)** ([Source](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16))  
  Qwen3.8-27B-DSpine-b16 is a text generation model from tencent. DSpine generates draft tokens in parallel. Each layer passes predicted predecessor features to adjacent positions, carrying causal dependencies through network depth.

* **[thinkingmachines/Inkling-2-Small](./models/2026-11-14-inkling-2-small.md)** ([Source](https://huggingface.co/thinkingmachines/Inkling-2-Small))  
  Inkling-2-Small is a multimodal image and text understanding model from thinkingmachines. Inkling 2 Small is a general-purpose multimodal model that accepts text and image inputs and generates text outputs. It is intended for use in English and other languages, and across multiple coding languages. The model is designed to be used by developers building AI-powered applications, including agentic and tool-use systems, coding assistants, chatbots, and retrieval-augmented generation systems, and is suitable for general-purpose conversational use, instruction-following, and other natural language and vis...

* **[Zyphra/ZONOS3-Mini](./models/2026-11-13-zonos3-mini.md)** ([Source](https://huggingface.co/Zyphra/ZONOS3-Mini))  
  ZONOS3-Mini is a speech synthesis model from Zyphra. cloning with just 100 million active parameters. It runs in real time on phones and laptops, including directly in the browser.

* **[Cactus-Compute/mirage](./models/2026-11-13-mirage.md)** ([Source](https://huggingface.co/Cactus-Compute/mirage))  
  mirage is a multimodal image and text understanding model from Cactus-Compute. The package downloads and caches the engine and weights on first use.
<!-- MODELS:END -->

<p><a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/models/README.md">View all <!-- MODELS_COUNT -->24<!-- /MODELS_COUNT --> open-source models in archive →</a></p>

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
