import streamlit as st
import joblib
import pandas as pd

# تحميل الموديلات
model_tourist_number = joblib.load('weights/model_tourist_number.pkl')
model_model_value = joblib.load('weights/model_model_value.pkl')

# واجهة الموقع
st.sidebar.title("\ud83d\udcd6 About the App")
st.sidebar.info("""
Welcome to the **Tourism Prediction App**!  
This app predicts:
- **Number of Tourists Indicator**  
- **Tourism Income (SAR)**

Based on selected inputs like:  
- Province  
- Tourism Type  
- Indicator  
- Year  
- Month  
""")
st.sidebar.markdown("---")

st.title("\ud83e\uddf3 Welcome To Murtad")
st.header("Customize Your Tourism Forecast:")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5dc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# واجهة الادخال
c1, c2 = st.columns(2)

with c1:
    year = st.selectbox("Select Year", list(range(2020, 2031)))
    province = st.selectbox("Select Province", ['Province A', 'Province B', 'Province C'])

with c2:
    month = st.selectbox("Select Month", list(range(1, 13)))
    tourism_type = st.selectbox("Select Tourism Type", ['Type A', 'Type B', 'Type C'])

indicator = st.selectbox("Select Indicator", ['Number of Tourists', 'Tourism Income'])

# زر التنبؤ
if st.button('Predict'):

    # تجهيز الدخل (حل المشكلة هنا!)
    input_df = pd.DataFrame({
        'Province': [province],
        'Tourism Type': [tourism_type],
        'Indicator': [indicator],
        'Year': [int(year)],
        'Month': [int(month)]
    })

    # توقع على حسب المؤشر
    if indicator == 'Number of Tourists':
        prediction = model_tourist_number.predict(input_df)[0]
        st.success(f"Predicted Number of Tourists: {prediction:,.0f}")
    else:
        prediction = model_model_value.predict(input_df)[0]
        st.success(f"Predicted Tourism Income (SAR): {prediction:,.2f}")
