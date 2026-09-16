import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
# ۱. آماده‌سازی عکس‌ها (تبدیل به تنسور و نرمال‌سازی)
transform = transforms.Compose([transforms.ToTensor()])

# ۲. دانلود دیتای اعداد دست‌نویس
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# ۳. برداشتن یک دسته (Batch) از عکس‌ها برای تست
dataiter = iter(trainloader)
images, labels = next(dataiter)

print(f"Shape of images in one batch: {images.shape}") # باید [64, 1, 28, 28] باشد



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

# ۱. دانلود داده‌های تست (که مدل در آموزش ندیده بود)
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

correct = 0
total = 0

# ۲. غیرفعال کردن محاسبه مشتق برای سرعت بیشتر و صرفه‌جویی در رم
with torch.no_grad():
    for images, labels in testloader:
        outputs = model(images)
        # پیدا کردن ایندکسی که بیشترین امتیاز را دارد
        _, predicted = torch.max(outputs.data, 1)
        
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the 10000 test images: {100 * correct / total}%')