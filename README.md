<div align="center">
  <h1>Model & Paper</h1>
  <p><strong>Trending open-source machine learning models and research papers, updated daily.</strong></p>

<!-- COUNTERS:START -->
<p align="center">
  <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/papers/README.md"><img src="https://img.shields.io/badge/Papers-19%20Indexed-2563eb?style=flat-square" alt="Papers Count"></a>
  <a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/models/README.md"><img src="https://img.shields.io/badge/Models-20%20Indexed-16a34a?style=flat-square" alt="Models Count"></a>
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
* **[SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models](./papers/2026-11-13-so-arena-benchmarking-the-capability-spectrum-and-reliabilit.md)** ([Source](https://huggingface.co/papers/2611.15777))  
  System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited insight into the breadth of model capabilities and the reliability of their decisions.

* **[MMDM: Measuring Massive Multitask Decision Making](./papers/2026-11-12-mmdm-measuring-massive-multitask-decision-making.md)** ([Source](https://huggingface.co/papers/2611.14309))  
  System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on existing benchmarks, where prior exposure to test material can obscure generalization. Moreover, real-world decision making often involves long contexts, large option spaces, and complex logical dependencies, challenges that existing be...

* **[Few-Step Streaming Video Generation via Condition Shifting](./papers/2026-11-12-few-step-streaming-video-generation-via-condition-shifting.md)** ([Source](https://huggingface.co/papers/2611.14033))  
  Few-step sampling reduces the cost of streaming video generation. Distribution Matching Distillation (DMD) supervises few-step generators with a separate fake-score network, which adds training memory and computation and must track the evolving generator. We extend APEX to streaming video by using condition shifting to estimate the velocity field of the generated distribution within the generator.

* **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](./papers/2026-11-11-tree-ising-repairing-language-models-with-bit-level-ising-ed.md)** ([Source](https://huggingface.co/papers/2611.14210))  
  Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-pass requests. Our method, Tree-Ising, casts this repair as a sparse discrete optimization problem over the model's own BF16 weights.

* **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](./papers/2026-11-11-don-t-just-trust-your-memory-evidence-linked-memory-reduces.md)** ([Source](https://huggingface.co/papers/2611.14320))  
  External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled only with task success or failure, yet are typically provided without the trajectories they came from...
<!-- PAPERS:END -->

<p><a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/papers/README.md">View all <!-- PAPERS_COUNT -->19<!-- /PAPERS_COUNT --> research papers in archive →</a></p>

---

## Latest Open-Source Models

<!-- MODELS:START -->
* **[Zyphra/ZONOS3-Mini](./models/2026-11-13-zonos3-mini.md)** ([Source](https://huggingface.co/Zyphra/ZONOS3-Mini))  
  ZONOS3-Mini is a speech synthesis model from Zyphra. cloning with just 100 million active parameters. It runs in real time on phones and laptops, including directly in the browser.

* **[Comfy-Org/MiniMax-H3-Image](./models/2026-11-12-minimax-h3-image.md)** ([Source](https://huggingface.co/Comfy-Org/MiniMax-H3-Image))  
  MiniMax-H3-Image is a text-to-image generation model from Comfy-Org. For prompt enhancement, we recommend to use the model qwen3.59bw4a8gptq with the Generate Text node.

* **[VideoRebirthAI/hyperflow-h3-flash](./models/2026-11-12-hyperflow-h3-flash.md)** ([Source](https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash))  
  hyperflow-h3-flash is a image text to video model from VideoRebirthAI. The transformer weights in this repository (both INT8 convrot and GGUF) are a Model Derivative of MiniMax-H3 and are distributed under the MiniMax H3 Community License Agreement with no additional terms. By downloading or using them, you accept that Agreement:

* **[Viggle/Viggle-Remake](./models/2026-11-11-viggle-remake.md)** ([Source](https://huggingface.co/Viggle/Viggle-Remake))  
  Viggle-Remake is a video to video model from Viggle. Viggle Remake is built agent-first. Give an agent (Claude Code, codex, anything that speaks MCP) a video and one

* **[MiniMaxAI/MiniMax-H3-Image](./models/2026-11-11-minimax-h3-image.md)** ([Source](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image))  
  MiniMax-H3-Image is a text-to-image generation model from MiniMaxAI. and developers a flexible and controllable way to create images.
<!-- MODELS:END -->

<p><a href="https://github.com/BELYAGOUBIABDELILAH/model-and-paper/blob/main/models/README.md">View all <!-- MODELS_COUNT -->20<!-- /MODELS_COUNT --> open-source models in archive →</a></p>

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
