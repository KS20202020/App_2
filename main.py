import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('008 images/photo.jpg')

with col2:
    st.title('Koushik Sarkar')
    content = """
    Hi, I am Koushik! Iam a Python programmer. I am a student of Khulna University of Engineering & Technology.
    I am trying to learn Python on my own and want to become a full fledged Python programmer. 
    """
    st.info(content)