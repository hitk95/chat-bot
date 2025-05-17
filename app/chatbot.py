import streamlit as st
from chatbot_core import get_response

st.title("Hit's Test AI Chatbot")
query = st.text_input("Ask me only about Canada! :")

if query:
    response = get_response(query)
    st.write(response)
