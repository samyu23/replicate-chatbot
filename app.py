import streamlit as st
import google.generativeai as genai

st.title("Welcome to gemini chat")

genai.configure(api_key="AIzaSyBDWHjTHHASRRq8535FpIbp2VZ3AoFq2Vw")
text=st.text_input("enter your question")
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

if st.button("Click me"):
    response=chat.send_message(text)
    st.write(response.text)