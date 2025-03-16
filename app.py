import streamlit as st
from utils.session_manager import initialize_session_state, get_llm_chain_from_session
from utils.llm_utils import get_llm
from utils.data_classes import Message
from components.sidebar import create_sidebar
from components.chat_interface import display_chat_messages, handle_chat_input

# Initialize session state and LLM chain
initialize_session_state()

# Create sidebar
create_sidebar()

# Main chat interface
st.title("🤖 Data Science Tutor Chat")

# Display chat messages
display_chat_messages(st.session_state["messages"])

# Handle chat input
handle_chat_input(st.session_state["messages"], get_llm_chain_from_session())