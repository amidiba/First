from transformers import Trainer, TrainingArguments

# ۱. تعریف تنظیمات آموزش
training_args = TrainingArguments(
    output_dir="./hafez_model",
    num_train_epochs=3,      # ۳ دور مرور اشعار حافظ
    per_device_train_batch_size=4,
    save_steps=100,          # هر ۱۰۰ قدم مدل را ذخیره کن
)

# ۲. استفاده از Trainer (ابزار هوشمند Hugging Face)
trainer = Trainer(
    model=model,             # همان مدل عمومی ما (مثل ParsBERT)
    args=training_args,
    train_dataset=hafez_dataset, # اشعار حافظ که به فرمت عدد درآمده‌اند
)

# ۳. شروع عملیات تراشکاری
trainer.train()