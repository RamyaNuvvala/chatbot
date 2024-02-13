import streamlit as st
import random

def chatbot_response(question):
    patterns_responses = {
        "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
        "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
        "college": ["Our college offers a variety of programs. What specific information are you looking for?"],
        "program": ["We offer programs in computer science, engineering, business, and more. What program are you interested in?"],
        "admissions": ["Our admissions office can assist you with the application process. Do you have any specific questions about admissions?"],
        # Add more patterns and responses as needed
    }
    for pattern, responses in patterns_responses.items():
        if pattern in question.lower():
            return random.choice(responses)
    return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    st.title("College Chatbot")
    questions = []

    with st.form(key='question_form'):
        user_input = st.text_input("Enter your question (type 'quit' to exit):", key='user_input')

        if st.form_submit_button("Ask"):
            if user_input.lower() == 'quit':
                st.stop()

            if user_input.strip():  # Check if input is not empty
                questions.append(user_input)
                response = chatbot_response(user_input)
                st.write(f"Question: {user_input}")
                st.write(f"Response: {response}")
                st.markdown("---")

    st.write("All questions asked and their responses:")
    for idx, question in enumerate(questions):
        response = chatbot_response(question)
        st.write(f"{idx + 1}. Question: {question} - Response: {response}")

if __name__ == "__main__":
    main()
    
