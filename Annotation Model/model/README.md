# CRSA Annotation Model (LoRA on Baichuan2-7B)

This folder contains the configuration and adapter files for the automatic annotation model used in the CRSA dataset.

## 🔗 Weights

Download the full model weight (`adapter_model.safetensors`) from:

[🔗 HuggingFace Link](https://huggingface.co/GrsXsa/CRSA-Annotation-baichuan2-7B/upload/main)

Place it in this folder.

## 🧩 Contents

- `adapter_config.json`
- `special_tokens_map.json`
- `checkpoint`
- (downloaded) `adapter_model.safetensors`

## 🧪 Usage

Use `run_inference.py` in the upper folder to run structure annotation on CRSA dialogues.
