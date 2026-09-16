import random

state = 0  # نقطه شروع
target = 42
q_table = {} # حافظه مدل برای هر عدد

def get_action(s):
    # قانون اپسیلون: ۱۰٪ مواقع ریسک کن، ۹۰٪ مواقع از حافظه استفاده کن
    if random.random() < 0.1 or s not in q_table:
        return random.choice(['+1', '-1'])
    return q_table[s]

# اینجا مدل با هزاران بار "بالا و پایین رفتن" یاد می‌گیرد
# که در هر عددی، کدام حرکت او را زودتر به ۴۲ می‌رساند.