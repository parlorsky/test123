max_length = 8
train_batch_size = 1
num_training_steps = 1000000
num_warmup_steps = 2000
initializer_range = 1e-2
lr = 2e-4
weight_decay = 1e-1
tokenizer_model_path = "configs/new_tokenizer.model"
patterns = ["data/pretrain_data/part-*.jsonl.zst"]
# global step
log_interval = 5
eval_interval = 200
save_interval = 800
work_dir = "data/saved_ckpt/"
