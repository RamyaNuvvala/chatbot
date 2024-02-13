import streamlit as st

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
            return responses

    return ["I'm sorry, I don't understand that. Can you please rephrase?"]

# Streamlit app
def main():
    st.title("College Chatbot")
    st.markdown("Welcome to our college chatbot! Feel free to ask questions.")

    conversation = st.session_state.get("conversation", [])
    
    # Initialize user input to an empty string
    user_input = ""
    
    # Get user input
    user_input = st.text_input("You:", value=user_input)
    
    if st.button("Send"):
        if user_input:
            # Add user input to the conversation history
            conversation.append(("You", user_input))
            # Get bot response
            bot_response = chatbot_response(user_input)
            # Add bot response to the conversation history
            conversation.append(("Bot", bot_response[0]))
            # Clear the input field by setting user_input to an empty string
            user_input = ""

    # Display conversation history
    st.markdown("---")
    st.markdown("**Conversation History**")
    for sender, message in conversation:
        st.write(f"{sender}: {message}")

    # Update conversation in session state
    st.session_state.conversation = conversation

if __name__ == "__main__":
    main()
