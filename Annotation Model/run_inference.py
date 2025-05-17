import json
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import torch

# 加载 PEFT 配置
config = PeftConfig.from_pretrained("model")
base_model_name = config.base_model_name_or_path

# 加载 tokenizer 和 base model
tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
base_model = AutoModelForCausalLM.from_pretrained(base_model_name, device_map="auto", torch_dtype=torch.float16)
model = PeftModel.from_pretrained(base_model, "model")

model.eval()

# 加载测试数据
with open("sample_Trainingdata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

results = []

for example in data:
    prompt = f"{example['instruction']}\n{example['input']}"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=1024)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    results.append({
        "input": example["input"],
        "output": response
    })

# 输出到文件
with open("inference_output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Inference completed. Output saved to inference_output.json")
