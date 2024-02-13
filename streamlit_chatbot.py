import streamlit as st
import time

def college_chatbot(question):
    question = question.lower()
    if "admissions" in question:
        return "For admissions information, please visit the college website or contact the admissions office."
    elif "courses" in question:
        return "You can find information about courses offered on the college website or in the course catalog."
    elif "campus" in question:
        return "The college campus is located at [Campus Address]. It includes various facilities such as libraries, laboratories, and sports facilities."
    elif "events" in question:
        return "You can stay updated about college events by checking the college website or following official social media channels."
    elif "housing" in question or "accommodation" in question:
        return "For information about housing options, you can contact the college housing office or visit the college website."
    else:
        return "I'm sorry, I don't have information about that. Please contact the college administration for further assistance."

def main():
    st.title("College Chatbot")

    question = st.text_input("You:")
    if st.button("Ask"):
        if question.strip():
            response = college_chatbot(question)
            st.write("College Chatbot:", response)
            st.text_input("You:")  # Clearing the input field after asking a question
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
        
