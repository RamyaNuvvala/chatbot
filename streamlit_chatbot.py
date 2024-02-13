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

    # Initialize conversation history from session state or create new if not exists
    conversation = st.session_state.get("conversation", [])
    questions = st.session_state.get("questions", [])

    # Get user input for each question
    question = st.text_input("Question:", value="")
    if st.button("Ask Question"):
        if question:
            # Get bot response
            bot_response = chatbot_response(question)
            # Append question and bot response to conversation history and questions
            conversation.append((question, bot_response))
            questions.append(question)
            # Clear input field after asking question
            st.session_state.question = ""

    # Display conversation history
    st.markdown("---")
    st.markdown("**Conversation History**")
    for question, bot_response in conversation:
        st.write(f"Question: {question}")
        st.write(f"Response: {bot_response}")

    # Update conversation history and questions in session state
    st.session_state.conversation = conversation
    st.session_state.questions = questions

if __name__ == "__main__":
    main()
