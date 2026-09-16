from torchvision import datasets, transforms
transform= transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
dataset=datasets.ImageFolder(root="/content/dataset", transform=transform)
print(dataset.classes)
print(len(dataset))
from torchvision import datasets, transforms

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

dataset = datasets.ImageFolder(
    root="/content/dataset",
    transform=transform
)

print(dataset.classes)
print(len(dataset))

import torch
import torchvision
from torchvision import transforms

# ۱. تغییراتی که باید روی هر عکس اعمال شود (پیش‌پردازش)
# عکس‌های شخصی اندازه‌های مختلفی دارند، همه را باید یک‌اندازه کنیم (مثلا 64x64)
transform = transforms.Compose([
    transforms.Resize((64, 64)),  # تغییر سایز اجباری
    transforms.ToTensor()         # تبدیل به ماتریس اعداد بین ۰ و ۱
])

# ۲. خواندن اتوماتیک عکس‌ها از پوشه
# ImageFolder خودش می‌فهمد که هر پوشه یک کلاس (تارگت) است
dataset = torchvision.datasets.ImageFolder(root='./dataset', transform=transform)

# ۳. نمایش اطلاعات
print(f"تعداد کل عکس‌ها: {len(dataset)}")
print(f"کلاس‌های پیدا شده: {dataset.classes}") # باید ['with_mask', 'without_mask'] باشد