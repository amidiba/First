import torch

# ذخیره کردن وزن‌های مدل
torch.save(model.state_dict(), "my_model.pth")

# حالا هر وقت بخواهی، فقط ساختار را می‌سازی و وزن‌ها را بارگذاری می‌کنی
# model.load_state_dict(torch.load("my_model.pth"))
import streamlit as st

st.title("سیستم تشخیص ماسک")
uploaded_file = st.file_uploader("یک عکس انتخاب کن...")

if uploaded_file:
    # عکس را به مدل می‌دهیم و نتیجه را چاپ می‌کنیم
    prediction = predict_mask(uploaded_file, model)
    st.write(f"نتیجه: {prediction}")