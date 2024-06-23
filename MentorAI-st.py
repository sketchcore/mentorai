import streamlit as st
import datetime

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'memories' not in st.session_state:
    st.session_state.memories = []

def add_message(message, is_user):
    st.session_state.messages.append({"message": message, "is_user": is_user, "timestamp": datetime.datetime.now()})

def add_memory(category, content):
    st.session_state.memories.append({"category": category, "content": content})

def delete_memory(index):
    st.session_state.memories.pop(index)

# Set page config
st.set_page_config(page_title="MentorAI", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: ##3A3A3A;
    }
    .main {
        background-color: ##3A3A3A;
        color: #333;
    }
    .chat-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .chat-message {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #ffdab9;
        align-self: flex-end;
    }
    .bot-message {
        background-color: #e6e6e6;
        align-self: flex-start;
    }
    .memory-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
    }
    .memory-item {
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .stTextInput>div>div>input {
        background-color: white;
        color: #333;
        border: 1px solid #ccc;
    }
    .stButton>button {
        background-color: #ff7f50;
        color: white;
    }
    .delete-btn {
        color: #ff4500;
        cursor: pointer;
    }
    .user-avatar {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-image: url('https://example.com/avatar.jpg');
        background-size: cover;
    }
</style>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([7, 3])

with col1:
    st.markdown("<h2 style='color: #ff7f50;'>MentorAI</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        # Display chat messages
        for message in st.session_state.messages:
            st.markdown(f"<div class='chat-message {'user-message' if message['is_user'] else 'bot-message'}'><strong>{'You' if message['is_user'] else 'MentorAI'}:</strong> {message['message']}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Chat input
    user_input = st.text_input("Type your message here...", key="user_input")
    if st.button("Submit"):
        if user_input:
            add_message(user_input, True)
            # Simulate AI response (replace with actual AI logic)
            ai_response = "Thank you for sharing. Can you tell me more?"
            add_message(ai_response, False)
            add_memory("User Input", user_input)
            st.rerun()

with col2:
    st.markdown("<h3 style='color: #ff7f50;'>Long-Term Memories</h3>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="memory-container">', unsafe_allow_html=True)
        for index, memory in enumerate(st.session_state.memories):
            st.markdown(f"""
            <div class='memory-item'>
                <strong>{memory['category']}:</strong> {memory['content']}
                <span class='delete-btn' onclick="this.parentElement.style.display='none'">✕</span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# User avatar
st.markdown("<div class='user-avatar'></div>", unsafe_allow_html=True)

# Copyright notice
st.markdown("<div style='position: fixed; bottom: 10px; left: 10px; font-size: 12px; color: #666;'>© 2024 Sketchcore Labs</div>", unsafe_allow_html=True)