# CRSA Auto-Annotation Model

This directory contains the automatic annotation model for the CRSA dataset. The model is fine-tuned using [LLaMA-Factory](https://github.com/hiyouga/llama-factory) with **LoRA** on top of **Baichuan2-7B**, enabling structured annotation generation from raw dialogue data.

The model takes multi-turn user-system dialogues as input and outputs structured JSON annotations aligned with CRSA’s three-layer schema (Context, Dialogue, Slots).

---

## 📌 Overview

- **Base model**: Baichuan2-7B-Chat
- **Fine-tuning framework**: LLaMA-Factory with PEFT (LoRA)
- **Task**: Structured labeling of task-oriented dialogue
- **Input**: Raw multi-turn dialogues in Chinese
- **Output**: Structured annotations with CRSA-compatible JSON format

---

## 🧪 Training Details

- **Dataset**: NewDialogue_train01 (derived from CRSA)
- **LoRA method**: Applied to selected layers with rank reduction
- **Training duration**: 3 epochs on multi-GPU setup
- **Batch sizes**: 2 (per device), gradient accumulation to 8
- **Learning rate**: 5e-5 with cosine decay scheduler
- **Mixed precision**: Native AMP enabled

Frameworks used:
- PEFT: 0.11.1
- Transformers: 4.41.0
- PyTorch: 2.3.0 + CUDA 12.1
- Datasets: 2.19.1

---

## 📂 Files

| File | Description |
|------|-------------|
| `run_inference.py`       | Run the model to annotate raw input dialogues |
| `model_utils.py`         | LoRA model loading and prompt formatting |
| `lora_config.json`       | LoRA configuration used in training |
| `sample_input.json`      | Example unannotated dialogue |
| `sample_output.json`     | Model-generated structured annotation |
| `training_card.md`       | Original model card generated from LLaMA-Factory |
| `requirements.txt`       | Inference-time dependencies |

---

## 🚀 Run Inference

```bash
python run_inference.py \
  --input sample_input.json \
  --output sample_output.json \
  --model_dir ./model/checkpoint
