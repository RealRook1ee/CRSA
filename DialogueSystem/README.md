# CRSA Dialogue System (Baichuan2-7B + LoRA)

This directory contains the training, merging, and inference pipeline for the CRSA dialogue system, which generates system replies based on structured dialogue history.

The model is trained using [LLaMA-Factory](https://github.com/hiyouga/llama-factory) with LoRA on top of `baichuan2-7B-chat`.

---

## 🔗 Model

The trained model weights are hosted on HuggingFace:

👉 [https://huggingface.co/GrsXsa/CRSA-dialogue-baichuan2-7B](https://huggingface.co/GrsXsa/CRSA-dialogue-baichuan2-7B)

---

## 🧠 Model Description

This model is fine-tuned from Baichuan2-7B using the CRSA dataset and is capable of transforming structured annotations into high-quality system responses. To fully utilize the multi-layer annotations in CRSA, we designed a multi-source input framework that guides natural language generation with rich contextual semantics.

The model receives four types of input:

- **T**: Task Prompt – includes task description, database documents, formatting guidelines, and few-shot examples.
- **H**: Historical Dialogue – full multi-turn context between user and system across all stages.
- **M**: Annotations – structured fields like dialogue states, stages, and semantic analysis.
- **K**: Key Annotations – explicitly highlighted features including user anomalies ($K_{\text{a}}$) and system actions ($K_{\text{s}}$) to control system behavior.

In accordance with Section 4.3 of our paper, the model gives particular attention to $K_{\text{a}}$ and $K_{\text{s}}$, which are the primary drivers of context-aware and goal-aligned response generation.

The conditional generation objective is:

\[
P(Y \mid T, H, M, K)
\]

The model is trained to optimize a weighted log-likelihood objective:

\[
\mathcal{L}(\theta) = \sum_{i=1}^{N} \left[ \alpha \cdot \log P(Y_i \mid K_i; \theta) + \beta \cdot \log P(Y_i \mid T_i, H_i, M_i; \theta) \right]
\]

where $\alpha > \beta$ emphasize the contribution of key annotations. Manual and automatic evaluation show that $\alpha:\beta = 2:1$ yields the best performance in slot coverage, annotation fidelity, and language fluency.

A staged training strategy is used:
1. Pretrain on (T, H, M) to build general understanding;
2. Focused tuning on $K_{\text{a}}$, $K_{\text{s}}$;
3. Final training on full input.

---

## 🏗️ Pipeline Overview

###  LoRA Fine-tuning

Use `scripts/train.sh` to fine-tune with your own CRSA-style data.

```bash
bash scripts/train.sh

Merge LoRA into full model to produce a standalone model compatible with transformers.

Run Inference

python scripts/infer.py \
  --model_path ./merged \
  --input data/sample.json

