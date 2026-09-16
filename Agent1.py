import gymnasium as gym

# ۱. ساخت محیط بازی
env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()

for _ in range(1000):
    # ۲. تصمیم‌گیری (فعلاً شانسی - همان Exploration خالص)
    action = env.action_space.sample() 
    
    # ۳. انجام عمل در محیط و گرفتن نتیجه
    observation, reward, terminated, truncated, info = env.step(action)
    
    # اگر چوب افتاد، بازی را دوباره شروع کن
    if terminated or truncated:
        observation, info = env.reset()

env.close()