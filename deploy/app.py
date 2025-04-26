
import streamlit as st
import joblib
import pandas as pd

model_tourist_number = joblib.load('weights/model_tourist_number.pkl')
model_model_value = joblib.load('weights/model_model_value.pkl')

st.sidebar.title("📘 About the App")
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

🔍 Use the options to explore different scenarios.
""")
st.sidebar.markdown("---")

st.title("🧳 Welcome To Murtad ")

st.header("Customize Your Tourism Forecast :")

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

c1, c2 = st.columns(2)

with c1:
    year = st.selectbox("Select Year", list(range(2020, 2030)))  
    month = st.selectbox("Select Month", list(range(1, 13)))  

    province = st.selectbox("Select Province", [
        'Al Bahah', 'AlQassim', 'AlQassim Province', 'Albaha province',
        'Aseer', 'Aseer Province', 'Eastern Province', 'Hail',
        'Hail Province', 'Jazan', 'Jazan Province', 'Jouf',
        'Jouf Province', 'Madinah', 'Madinah Province', 'Makkah',
        'Makkah Province', 'Najran', 'Najran Province', 'Northern Borders',
        'Northern Borders Province', 'Riyadh', 'Riyadh Province', 'Tabuk',
        'Tabuk Province', 'Total'
    ])

with c2:
    indicator = st.selectbox("Select Indicator", [
        "Overnight Visitors", "SAR"
    ])

    tourism_type = st.selectbox("Select Tourism Type", [
        "domestics_tourism", "inbound_tourism"
    ])

if st.button("Predict"):

    input_df = pd.DataFrame({
        'year': [year],
        "Province": [province],
        "Indicator": [indicator],
        "tourism type": [tourism_type],
        'month':[month]
    })

    prediction = model_tourist_number.predict(input_df)[0]
    prediction2 = model_model_value.predict(input_df)[0]

    st.success(f"📈 Predicted Tourists Indicator:  **{prediction:,.0f}** Indicators")
    st.success(f"💰 Predicted Income Value:  **{prediction2:,.0f}** SAR")

    with st.expander("🔍 View Input Data"):
        st.write(input_df)

st.markdown("---")
