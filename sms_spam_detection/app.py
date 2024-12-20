import streamlit as st
import pickle
import string
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Ensure required NLTK resources are available
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

ps = PorterStemmer()

def transform_text(text):
    # Lowercase the text
    text = text.lower()
    # Tokenize
    text = nltk.word_tokenize(text)
    # Remove non-alphanumeric tokens
    text = [word for word in text if word.isalnum()]
    # Remove stopwords and punctuation
    text = [word for word in text if word not in stopwords.words('english')]
    # Stem the words
    text = [ps.stem(word) for word in text]
    # Join back into a single string
    return " ".join(text)

# Get the current directory (the folder where the main app resides)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved TF-IDF vectorizer and trained model
try:
    tfidf = pickle.load(open(f'{current_dir}/vectorizer.pkl', 'rb'))
    model = pickle.load(open(f'{current_dir}/model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Required files (`vectorizer.pkl` or `model.pkl`) are missing. Please add them to the working directory.")
    st.stop()

# Streamlit app UI
st.title("Email/SMS Spam Classifier")

# Input text box
input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    if input_sms.strip():
        # Preprocess the input
        transformed_sms = transform_text(input_sms)
        # Vectorize the input
        try:
            vector_input = tfidf.transform([transformed_sms])
        except Exception as e:
            st.error(f"Error with vectorizer: {e}")
            st.stop()
        
        # Predict using the model
        try:
            result = model.predict(vector_input)[0]
        except Exception as e:
            st.error(f"Error with model prediction: {e}")
            st.stop()

        # Display the result
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")
    else:
        st.warning("Please enter a valid message.")
