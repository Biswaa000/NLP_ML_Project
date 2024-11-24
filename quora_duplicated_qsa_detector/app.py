
import streamlit as st
import helper
import pickle
import os

# Get the current directory (the folder where the main app resides)
current_dir = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(f'{current_dir}/model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')