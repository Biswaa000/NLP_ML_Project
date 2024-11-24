import streamlit as st

# Main Header
st.header('---All NLP ML PROJECTS---')

# Container for projects
with st.container():
    st.subheader("1. SMS Spam Detector")
    st.write("An app to detect whether an SMS is spam or not.")
    st.markdown("[Go to SMS Spam Detector](https://smsemail-spam-detector.streamlit.app/)", unsafe_allow_html=True)

with st.container():
    st.subheader("2. Quora Question Duplicate Detector")
    st.write("An app to detect duplicate questions on Quora.")
    st.markdown("[Go to Quora Duplicate Detector](https://quora-duplicated-qsa-detector.streamlit.app/)", unsafe_allow_html=True)

# Add more projects here
