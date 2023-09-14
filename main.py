import streamlit as st
from ChatController import ChatController
from Authentication import check_password
# Streamlit Configuration
st.set_page_config(page_title="Chat with Professor")

# Initialize ChatController
if "controller" not in st.session_state:
    st.session_state.controller = ChatController()
controller = st.session_state.controller

# Security
if not check_password():
    st.stop()

# Welcome Message
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.messages = [
        {
            "role": "Professeur",
            "content": "Bonjour! Bienvenue au cours SYST1046. Comment ça va aujourd'hui?",
        }
    ]

# Display Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input
user_input = st.chat_input()

if user_input:
    with st.chat_message("Étudiant"):
        st.write(user_input)
    st.session_state.messages.append({"role": "Étudiant", "content": user_input})

    responses = controller.process_message(user_input)

    # In case the response is just a single string (backward compatibility)
    if not isinstance(responses, list):
        responses = [responses]

    for response in responses:
        with st.chat_message("Professeur"):
            st.write(response)
        st.session_state.messages.append({"role": "Professeur", "content": response})
