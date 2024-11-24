import streamlit as st
import subprocess
import os

# Main Header
st.header('---All NLP ML PROJECTS---')

# Get the current directory (the folder where the main app resides)
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
print("----------------------------------------------")
# Function to run sub-app
def run_sub_app(relative_path):
    """Run a Streamlit app using a relative path."""
    app_path = os.path.join(current_dir, relative_path)  # Construct the full path
    subprocess.Popen(["streamlit", "run", app_path], shell=True)

# Container for projects
with st.container():
    st.subheader("1. Quora Question Duplicate Detector")
    st.write("An app to detect duplicate questions on Quora.")
    if st.button("Open Quora Duplicate Detector"):
        run_sub_app("quora_duplicated_qsa_detector/app.py")  # Relative path to the sub-app


with st.container():
    st.subheader("1. SMS Spam Detector")
    st.write("An app to detect whether an SMS is spam or not.")
    if st.button("Open SMS Spam Detector"):
        run_sub_app("sms_spam_detection/app.py")

 