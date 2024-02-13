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
def chatbot_response(user_input, conversation):
    for pattern, responses in patterns_responses.items():
        if pattern in user_input.lower():
            conversation.append(("You", user_input))
            bot_response = responses
            conversation.append(("Bot", bot_response))
            return conversation

    conversation.append(("You", user_input))
    conversation.append(("Bot", "I'm sorry, I don't understand that. Can you please rephrase?"))
    return conversation

# Streamlit app
def main():
    st.title("College Chatbot")
    st.markdown("Welcome to our college chatbot! Feel free to ask questions.")

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("You:", key="user_input", value="\n".join([msg[1] for msg in st.session_state.conversation if msg[0] == "You"]))
    
    if st.button("Send"):
        if user_input:
            st.session_state.conversation = chatbot_response(user_input, st.session_state.conversation)
            # Update URL query parameters with the updated session state
            st.experimental_set_query_params(**{"user_input": ""})

    # Display conversation history
    st.markdown("---")
    st.markdown("**Conversation History**")
    for sender, message in st.session_state.conversation:
        st.write(f"{sender}: {message}")

if __name__ == "__main__":
    main()
