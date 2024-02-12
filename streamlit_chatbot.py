import streamlit as st
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm good, thank you!", "I'm doing well, how about you?"]),
    (r"what is your name?", ["You can call me Chatbot.", "I'm just a chatbot."]),
    (r"what can you do?", ["I can provide information about courses, campus facilities, and more."]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]),
]

# Create a Chat object
chatbot = Chat(patterns, reflections)

# Define function to generate chat interface
def chat_interface():
    st.title("Basic Chatbot")
    st.markdown("Welcome! How can I assist you today?")
    user_input = st.text_input("You:")
    if st.button("Send"):
        response = chatbot.respond(user_input)
        st.text_area("Chatbot:", value=response, height=100)

# Main function to run the app
if __name__ == "__main__":
    chat_interface()
    
