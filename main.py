import streamlit as st
import pandas as pd
import os
from pathlib import Path
import spacy
from spacy import displacy

LOAD_MODEL_FROM = 'long_v14.h5'

# LOAD MODEL
if LOAD_MODEL_FROM:
    model.load_weights(f'{LOAD_MODEL_FROM}/long_v{VER}.h5')
    

st.markdown("<h1><em>ArguSense: Intelligent NLP-driven Argument Evaluation and Effectiveness Analysis</em></h1>", unsafe_allow_html=True)

st.subheader("Enter your prompt in the textbox below")


# Add a textbox to the app
user_input = st.text_area("Enter your text:", "Default text", height=400)


def save_file_to_test(example):
         # Create the "/test" folder if it doesn't exist
    if not os.path.exists("test"):
        os.makedirs("test")

    # Add a multiline textbox to get user input
    user_input = st.text_area("Enter your text:", "Default text", height=200)

    # Save user input to a text file in the "/test" folder
    with open("test/user_input.txt", "w") as file:
        file.write(user_input)

    # Display a confirmation message
    st.write("User input has been saved to 'test/user_input.txt'.")

if st.button("Proceed"):
        # Display the input
        st.write(user_input)
        save_file_to_test(user_input)