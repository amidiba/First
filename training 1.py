import torch.optim as optim

# ۱. ساخت مدل، تعریف تابع خطا و بهینه‌ساز
model = DigitClassifier()
criterion = nn.CrossEntropyLoss() # این تابع برای دسته‌بندی (۰ تا ۹) عالی است
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ۲. شروع آموزش برای ۵ دور (Epoch)
for epoch in range(5):
    running_loss = 0.0
    for images, labels in trainloader:
        # صفر کردن مشتق‌ها
        optimizer.zero_grad()
        
        # ۱. حدس زدن (Forward)
        outputs = model(images)
        
        # ۲. محاسبه خطا
        loss = criterion(outputs, labels)
        
        # ۳. مشتق‌گیری (Backward)
        loss.backward()
        
        # ۴. تغییر وزن‌ها (Update)
        optimizer.step()
        
        running_loss += loss.item()
    
    print(f"Epoch {epoch+1}, Loss: {running_loss/len(trainloader)}")

print("Finished Training!")