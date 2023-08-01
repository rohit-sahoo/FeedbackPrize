import streamlit as st

st.markdown("<h1><em>ArguSense: Intelligent NLP-driven Argument Evaluation and Effectiveness Analysis</em></h1>", unsafe_allow_html=True)

st.subheader("Enter your prompt in the textbox below")

# Add a textbox to the app
user_input = st.text_input("Enter your name:", "John Doe")

if st.button("Proceed"):
        # Display the input
        st.write(f"Hello, {user_input}!")