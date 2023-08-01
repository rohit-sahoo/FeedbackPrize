import streamlit as st
import pandas as pd
import os
from pathlib import Path
import spacy
from spacy import displacy


st.markdown("<h1><em>ArguSense: Intelligent NLP-driven Argument Evaluation and Effectiveness Analysis</em></h1>", unsafe_allow_html=True)

st.subheader("Enter your prompt in the textbox below")


# Add a textbox to the app
user_input = st.text_area("Enter your text:", "Default text", height=400)


"""


colors = {
            'Lead': '#8000ff',
            'Position': '#2b7ff6',
            'Evidence': '#2adddd',
            'Claim': '#80ffb4',
            'Concluding Statement': 'd4dd80',
            'Counterclaim': '#ff8042',
            'Rebuttal': '#ff0000'
         }


discourse_type = ['Lead',
 'Position',
 'Evidence',
 'Claim',
 'Concluding Statement',
 'Counterclaim',
 'Rebuttal']

def visualize(example):
    ents = []
    for i, row in train[train['id'] == example].iterrows():
        ents.append({
                        'start': int(row['discourse_start']), 
                        'end': int(row['discourse_end']), 
                        'label': row['discourse_type']
                    })

    doc2 = {
        "text": example,
        "ents": ents,
        "title": "Your passage"
    }

    options = {"ents": discourse_type, "colors": colors}
    displacy.render(doc2, style="ent", options=options, manual=True, jupyter=True)

"""


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