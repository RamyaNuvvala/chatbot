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

    # Get user input for each question
    questions = []
    while st.button("Ask Question"):
        question = st.text_input("Question:", value="")
        if question:
            questions.append(question)

    # Process user questions and get bot responses
    bot_responses = [chatbot_response(question) for question in questions]

    # Display questions and responses
    st.markdown("---")
    st.markdown("**Conversation History**")
    for question, response in zip(questions, bot_responses):
        st.write(f"Question: {question}")
        st.write(f"Response: {response}")

if __name__ == "__main__":
    main()
