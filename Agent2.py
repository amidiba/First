import numpy as np
import random

# تنظیمات محیط
size = 10  # طول مسیر
target = 9 # هدف در انتهای مسیر است
q_table = np.zeros(size) # جدول حافظه (برای هر مکان، یک امتیاز)

learning_rate = 0.1
gamma = 0.9      # ضریب آینده‌نگری
epsilon = 0.2    # میزان ریسک (Exploration)

# حلقه آموزش (۱۰۰ بار تمرین)
for episode in range(100):
    state = 0 # شروع از ابتدای مسیر
    while state < target:
        # ۱. انتخاب عمل (ریسک یا استفاده از تجربه؟)
        if random.random() < epsilon:
            action = 1 # ریسک: برو جلو
        else:
            # در این مثال ساده فقط حرکت به جلو داریم
            action = 1 
            
        next_state = state + action
        
        # ۲. تعریف پاداش
        if next_state == target:
            reward = 10 # جایزه بزرگ برای رسیدن به هدف
        else:
            reward = -1 # تنبیه کوچک برای هر قدم اضافه (تا سریع‌تر برسد)
            
        # ۳. فرمول جادویی بروزرسانی (Bellman)
        # امتیاز فعلی = امتیاز فعلی + (پاداش + امتیاز آینده - امتیاز فعلی)
        q_table[state] += learning_rate * (reward + gamma * q_table[next_state] - q_table[state])
        
        state = next_state

print("حافظه مدل بعد از تمرین (Q-Table):")
print(q_table)