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

    # Initialize conversation history
    conversation = st.session_state.get("conversation", [])

    # Get user input for each question
    question = st.text_input("Ask a question:")
    if st.button("Ask"):
        if question:
            # Get bot response
            bot_response = chatbot_response(question)
            # Append question and bot response to conversation history
            conversation.append((question, bot_response))
            # Display bot response
            st.write(f"Response: {bot_response}")

    # Display conversation history
    st.markdown("---")
    st.markdown("**Conversation History**")
    for q, a in conversation:
        st.write(f"Question: {q}")
        st.write(f"Response: {a}")

    # Update conversation history in session state
    st.session_state.conversation = conversation

if __name__ == "__main__":
    main()
