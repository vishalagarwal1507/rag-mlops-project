import streamlit as st
import requests

st.title("RAG Chatbot")

# Initialize state
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to handle submit
def submit():
    query = st.session_state.user_input

    if query:
        # Save user message
        st.session_state.messages.append(("You", query))

        # API call
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": query}
        )

        answer = response.json()["answer"]

        # Save bot message
        st.session_state.messages.append(("Bot", answer))

        # Clear input safely
        st.session_state.user_input = ""

# Input box
st.text_input("You:", key="user_input")

# Button with callback
st.button("Send", on_click=submit)

# Display chat
for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")
