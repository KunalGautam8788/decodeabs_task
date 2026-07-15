import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

# -------------------------------
# Configure Gemini
# -------------------------------
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="JARVIS AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.stChatMessage {
    border-radius: 12px;
    padding: 10px;
}

h1 {
    text-align: center;
}

.user-msg {
    color: white;
}

.bot-msg {
    color: #E6E6E6;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.title("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown("""
    ### About
    👋 Hello! I'm Jarvis,
    your AI assistant.

I'm here to help you with questions,
ideas, 
problem-solving, and much more.

Ask me anything,
and I'll do my best to assist you!

   
    """)

# -------------------------------
# Main Header
# -------------------------------
st.title("🤖JARVIS AI Chatbot")
st.caption("Ask anything and chat with Gemini")

# -------------------------------
# Initialize Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Display Previous Messages
# -------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# User Input
# -------------------------------
prompt = st.chat_input("Type your message here...")

if prompt:

    # Show User Message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    try:
        with st.spinner("Thinking..."):

            response = model.generate_content(prompt)

            bot_response = response.text

        # Display Bot Message
        with st.chat_message("assistant"):
            st.markdown(bot_response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": bot_response
            }
        )

    except Exception as e:
        st.error(f"Error: {e}")