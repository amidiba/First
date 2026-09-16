import torch
import torch.nn as nn
import torch.nn.functional as F

class DigitClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        # ورودی ما ۷۸۴ پیکسل است (۲۸ در ۲۸)
        self.fc1 = nn.Linear(784, 128) 
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10) # ۱۰ خروجی برای اعداد ۰ تا ۹

    def forward(self, x):
        # پهن کردن تصویر (Flatten)
        x = x.view(-1, 784) 
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = DigitClassifier()
print(model)