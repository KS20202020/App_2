import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('008 images/photo.jpg', width=550)

with col2:
    st.title('Koushik Sarkar')
    content1 = """
    Hi, I am Koushik! Iam a Python programmer. I am a student of Khulna University of Engineering & Technology.
    I am trying to learn Python on my own and want to become a full fledged Python programmer. 
    """
    st.info(content1)

content2 = """
    Below you can find some apps that i built in Python.
    Feel free to contact me!
    """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv('008 data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image('008 images/' + row['image'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image('008 images/' + row['image'])
        st.write(f"[Source code]({row['url']})")