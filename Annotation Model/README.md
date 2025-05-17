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

This model is designed to annotate raw user-system dialogues in CRSA format using instruction-based prompting. It follows the **instruction-tuning format** used by LLaMA-Factory, where each sample includes:

- instruction: task description + schema constraint
- input: raw dialogue content
- output: structured JSON annotation in CRSA format

To generate annotations for new dialogues:

bash
python run_inference.py \
  --input raw_dialogues.json \
  --output annotated_results.json \
  --model_dir ./model/checkpoint

## 🔹 Input Format
Each input sample must be a dictionary in the following structure:

{
  "instruction": "Please analyze and annotate the following dialogue. The output must follow the CRSA JSON format: {\"Context\": {\"basic_information\": {\"current_step\": true, \"utterances\": [], \"slots\": {\"destination\": \"\", \"departure\": \"\", \"airport\": \"\", \"departure_time\": \"\", \"airlines\": \"\", \"cabin\": \"\", \"price\": \"\", \"flight_duration\": \"\", \"arrival_time\": \"\"}}, \"ticket_selection\": {\"current_step\": false, \"utterances\": [], \"ticket_options\": [], \"user_choice\": {}}, \"booking_information\": {\"current_step\": false, \"utterances\": [], \"personal_information\": {\"name\": \"\", \"id_number\": \"\", \"phone_number\": \"\"}}}, \"Dialogue\": {\"agenda\": {\"current_step\": \"basic_information\", \"utterances\": \"\", \"analysis\": {\"question\": \"\", \"statements\": []}}, \"user\": {\"utterances\": \"\", \"anomaly_analysis\": {\"has_anomaly\": false, \"anomaly_reason\": \"\"}}}, \"Slots\": {\"destination\": \"\", \"departure\": \"\", \"airport\": \"\", \"departure_time\": \"\", \"airlines\": \"\", \"cabin\": \"\", \"price\": \"\", \"flight_duration\": \"\", \"arrival_time\": \"\"}}",
  "input": "系统：您好，请问您需要订票吗？\n用户：我想订一张从成都到拉萨的机票。\n......",
  "output": "{ \"Context\": {...}, \"Dialogue\": {...}, \"Slots\": {...} }"
}

## 📚 Notes
This model was trained using LLaMA-Factory with LoRA and instruction-tuning format.

You may batch multiple samples into one .json list file for inference.

Be sure the instruction clearly specifies the required output structure (e.g., CRSA schema).

Model supports both chat-style response and structured annotation generation.

## 🔗 Model Weights

Due to file size limitations, the model checkpoint file (`adapter_model.safetensors`) is hosted externally.

Please download it from the following link:

👉 [Download adapter_model.safetensors from HuggingFace](https://huggingface.co/GrsXsa/CRSA-Annotation-baichuan2-7B/tree/main/adapter_model.safetensors)

After downloading, place it in:

CRSA/Annotation Model/model/adapter_model.safetensors
把上述内容整理成README.md的格式输出
