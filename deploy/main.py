import streamlit as st
import os

def main():
    st.set_page_config(page_title="Murtad - From Data To Smart Moves", layout="centered")
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

    c1,c2,c3 = st.columns([1, 3, 1])
    with c1:
        st.write("")  
    with c2:
        st.image('deploy\imges.png', width=500)
    with c3:
        st.write("")


    st.markdown("""
        <div style='text-align: center; font-size: 18px;'>
        Here, data speaks the language of the future.<br>
        We reveal the stories behind the numbers behind destinations,<br>
        so your vision is clearer and your steps are smarter.<br>
        <b>Explore the future of tourism trends and spending in Saudi Arabia with AI-powered insights and predictions.</b>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Get Started"):
        os.system('streamlit run deploy/app.py')  

if __name__ == "__main__":
    main()
