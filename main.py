import streamlit as st


st.subheader("Enter your prompt in the textbox below")

# Add a textbox to the app
user_input = st.text_input("Enter your name:", "John Doe")

# Display the input
st.write(f"Hello, {user_input}!")