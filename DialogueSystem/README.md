# CRSA Dialogue System (Baichuan2-7B + LoRA)

This directory contains the training, merging, and inference pipeline for the CRSA dialogue system, which generates system replies based on structured dialogue history.

The model is trained using [LLaMA-Factory](https://github.com/hiyouga/llama-factory) with LoRA on top of `baichuan2-7B-chat`.

---

## 🚀 Model

The trained weights are hosted on HuggingFace:

👉 [https://huggingface.co/GrsXsa/CRSA-dialogue-baichuan2-7B](https://huggingface.co/GrsXsa/CRSA-dialogue-baichuan2-7B)

---

## 🏗️ Pipeline Overview

### 1. LoRA Fine-tuning

Use `scripts/train.sh` to fine-tune with your own CRSA-style data.

```bash
bash scripts/train.sh
---

### 2. Merge LoRA into full model

python scripts/merge.sh \
  --model_path ./trained \

This will produce a standard model compatible with transformers for deployment.

### 3. Run Inference

python scripts/infer.py \
  --model_path ./merged \
  --input data/sample.json

## 🧪 Training Configuration
Model: baichuan2-7B-chat

Platform: LLaMA-Factory

LoRA Rank: 8

Batch Size: 2 × 4 GPUs

Scheduler: cosine

Epochs: 3

Format: Instruction-tuning (single-round)

## 📄 License
This module is released under the CC BY 4.0 License.

