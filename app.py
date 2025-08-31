import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Hackathon Chatbot", page_icon="🤖")
st.title("🤖 Hackathon Chatbot")
st.write("Hi! Ask me anything!")

# Use a small, lightweight model
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

user_input = st.text_input("You:", "")

if user_input:
    response = chatbot(user_input, max_length=100)
    st.write("**Bot:**", response[0]['generated_text'])
