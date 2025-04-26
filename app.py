
import streamlit as st
import joblib
import pandas as pd

# Load models
model_tourist_number = joblib.load('weights/model_tourist_number.pkl')
model_model_value = joblib.load('weights/model_model_value.pkl')

# Apply font and styling
st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"]  {
    font-family: 'Tajawal', sans-serif;
    background: #fffdf5 !important;
    background-color: #fffdf5 !important;
}
.stApp {
    background-color: #fffdf5 !important;
}
.block-container {
    background-color: #fffdf5 !important;
}
.stButton > button {
    font-size: 18px;
    padding: 10px 25px;
    border-radius: 8px;
    background-color: #f63366;
    color: white;
    border: none;
}
h1.title-green {
    color: #567d46;
    text-align: center;
    font-size: 38px;
}
h3.custom-subtitle {
    font-size: 20px;
    color: #333333;
    margin-bottom: 25px;
}
</style>""", unsafe_allow_html=True)

# Page control
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# Welcome Page
if st.session_state.page == 'welcome':
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("img/murtad_logo.png", width=1000)

    st.markdown("""
        <div style="text-align: center;">
            <p style="font-size:16px;">
                Here, data speaks the language of the future.<br>
                We reveal the stories behind the numbers behind destinations,<br>
                so your vision is clearer and your steps are smarter.<br><br>
                Explore the future of tourism trends and spending in Saudi Arabia<br>
                with AI-powered insights and predictions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Get Started"):
        st.session_state.page = 'predict'

# Prediction Page
elif st.session_state.page == 'predict':
    st.markdown("<h1 class='title-green'>Welcome to Murtad</h1>", unsafe_allow_html=True)

    st.sidebar.title("📘 About the App")
    st.sidebar.info("""
    This app predicts:
    - **Number of Tourists**
    - **Tourism Income (SAR)**

    Based on:
    - Province
    - Tourism Type
    - Indicator
    - Year
    - Month
    """)
    st.sidebar.markdown("---")

    st.markdown("<h3 class='custom-subtitle'>Customize Your Tourism Forecast</h3>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        year = st.selectbox("Select Year", list(range(2020, 2030)))
        month = st.selectbox("Select Month", list(range(1, 13)))
        province = st.selectbox("Select Province", [
            'Al Bahah', 'AlQassim', 'Aseer', 'Eastern Province', 'Hail',
            'Jazan', 'Jouf', 'Madinah', 'Makkah', 'Najran',
            'Northern Borders', 'Riyadh', 'Tabuk', 'Total'])

    with c2:
        indicator = st.selectbox("Select Indicator", [
            "Overnight Visitors", "SAR"])
        tourism_type = st.selectbox("Select Tourism Type", [
            "domestics_tourism", "inbound_tourism"])

    if st.button("Predict"):
        input_data = pd.DataFrame({
            'year': [year],
            'month': [month],
            'Province': [province],
            'Indicator': [indicator],
            'tourism type': [tourism_type]
        })

        prediction1 = model_tourist_number.predict(input_data)[0]
        prediction2 = model_model_value.predict(input_data)[0]

        st.success(f"Predicted Number of Tourists: {int(prediction1):,}")
        st.success(f"Predicted Tourism Income (SAR): {prediction2:,.2f}")
