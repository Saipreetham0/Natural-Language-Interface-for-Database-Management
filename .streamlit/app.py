import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Summerizer" , page_icon=":mask:" , layout="centered")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding= load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_0o9pv7tm.json")
st.title(":blue[Video Transcript Summarizer]")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        a=st.radio("Choose method:",("Have a URL","Have the Audio File"))
        text_input=st.text_input("Enter URL:")
        st.write("##")
        st.write("[Learn more>](https://youtube.com)")
    with right_column:
        st_lottie(lottie_coding,height=109,key="coding")    
