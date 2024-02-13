import streamlit as st
import random

# Define patterns and corresponding responses
patterns_responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "college": ["Our college offers a variety of programs. What specific information are you looking for?"],
    "program": ["We offer programs in computer science, engineering, business, and more. What program are you interested in?"],
    "admissions": ["Our admissions office can assist you with the application process. Do you have any specific questions about admissions?"],
    # Add more patterns and responses as needed
}

# Function to find matching pattern and return response
def chatbot_response(user_input):
    for pattern, responses in patterns_responses.items():
        if pattern in user_input.lower():
            return random.choice(responses)

    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Streamlit app
def main():
    st.title("College Chatbot")
    st.markdown("Welcome to our college chatbot! Feel free to ask questions.")

    chat_history = st.session_state.get("chat_history", [])

    user_input = st.text_input("You:", key="user_input")
    if st.button("Send"):
        if user_input:
            bot_response = chatbot_response(user_input)
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
    
