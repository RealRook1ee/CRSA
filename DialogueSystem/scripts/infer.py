import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = "./trained"
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")

with open("sample.json", "r", encoding="utf-8") as f:
    samples = json.load(f)

for item in samples:
    prompt = f"{item['instruction']}\n{item['input']}"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output_ids = model.generate(**inputs, max_new_tokens=128)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print("🧾 System reply:", output_text)
