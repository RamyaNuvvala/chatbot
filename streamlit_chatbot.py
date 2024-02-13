import streamlit as st
import re
import random

# Define patterns and corresponding responses
patterns_responses = {
    r"hi|hello|hey": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    r"how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    r"college": ["Our college offers a variety of programs. What specific information are you looking for?"],
    # Add more patterns and responses as needed
}

# Function to find matching pattern and return response
def chatbot_response(user_input, chat_history):
    for pattern, responses in patterns_responses.items():
        if re.search(pattern, user_input.lower()):
            response = random.choice(responses)
            return response, chat_history

    return "I'm sorry, I don't understand that. Can you please rephrase?", chat_history

# Streamlit app
def main():
    st.title("Pattern Matching Chatbot")
    st.markdown("Welcome to our chatbot! Feel free to ask questions.")

    chat_history = st.session_state.get("chat_history", [])

    user_input = st.text_input("You:", key="user_input")
    if st.button("Send"):
        if user_input:
            bot_response, chat_history = chatbot_response(user_input, chat_history)
            chat_history.append(("You", user_input))
            chat_history.append(("Bot", bot_response))
            st.write(f"Bot: {bot_response}")
            st.session_state.chat_history = chat_history
            st.session_state.user_input = ""  # Clear input area

    # Display chat history
    st.markdown("---")
    st.markdown("**Chat History**")
    for sender, message in chat_history:
        st.write(f"{sender}: {message}")

if __name__ == "__main__":
    main()
    
