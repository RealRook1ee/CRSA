source ./anaconda3/etc/profile.d/conda.sh

conda activate llama_factory

CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch \
    --config_file ./LLaMA-Factory-main/examples/accelerate/single_config.yaml \
    /home/LAB/wangxf/LLaMA-Factory-main/src/train.py \
    --stage sft \
    --do_train True \
    --model_name_or_path /home/incoming/LLM/baichuan2/baichuan2-7b-chat \
    --finetuning_type lora \
    --quantization_bit 4 \
    --template baichuan2 \
    --flash_attn auto \
    --dataset_dir ./LLaMA-Factory-main/data \
    --dataset Crsa_train \
    --learning_rate 5e-05 \
    --num_train_epochs 3.0 \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --max_grad_norm 0.3 \
    --logging_steps 20 \
    --warmup_steps 0 \
    --lora_rank 128 \
    --save_steps 100 \
    --lora_dropout 0.05 \
    --lora_target q_proj,o_proj,k_proj,v_proj,down_proj,gate_proj,up_proj \
    --output_dir ./trained \
    --fp16 True \
    --plot_loss True

echo "Job ended on $(date)"
