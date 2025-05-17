
conda activate llama_factory

llamafactory-cli export \
    --model_name_or_path ./baichuan2/baichuan2-7b-chat \
    --adapter_name_or_path ./trained \
    --template baichuan2 \
    --finetuning_type lora \
    --export_dir ./dialoguesys \
    --export_size 2 \
    --export_legacy_format False
