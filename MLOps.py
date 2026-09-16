import torch

# ذخیره کردن وزن‌های مدل
torch.save(model.state_dict(), "my_model.pth")

import streamlit as st

st.title("سیستم تشخیص ماسک")
uploaded_file = st.file_uploader("یک عکس انتخاب کن...")

if uploaded_file:
    # عکس را به مدل می‌دهیم و نتیجه را چاپ می‌کنیم
    prediction = predict_mask(uploaded_file, model)
    st.write(f"نتیجه: {prediction}")
