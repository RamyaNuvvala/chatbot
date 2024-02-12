import streamlit as st
import spacy
from nltk.chat.util import Chat, reflections

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm good, thank you!", "I'm doing well, how about you?"]),
    (r"(.*) your name?", ["You can call me Chatbot.", "I'm just a chatbot."]),
    (r"what can you do?", ["I can provide information about courses, campus facilities, and more."]),
    (r"(CSE|computer science|computer engineering)", ["The Computer Science and Engineering (CSE) department offers various programs. You can find more information [here](cse_link)."]),
    (r"(ECE|electronics and communication engineering)", ["The Electronics and Communication Engineering (ECE) department offers various programs. You can find more information [here](ece_link)."]),
    (r"(college website|college site)", ["You can visit the college website [here](college_website_link)."]),
    (r"(moodle|online learning platform)", ["You can access Moodle [here](moodle_link)."]),
    (r"(notices|announcements)", ["You can check notices [here](notices_link)."]),
    (r"(academic calendar|schedule)", ["The academic calendar is available [here](academic_calendar_link)."]),
    (r"(placements|career opportunities)", ["For placements, visit [this link](placements_link)."]),
    (r"quit", ["Bye! Take care."]),
]

# Create a Chat object
chatbot = Chat(patterns, reflections)

# Define function to analyze user input using spaCy
def analyze_input(user_input):
    doc = nlp(user_input)
    tokens = [token.text for token in doc]
    # Add any additional analysis or processing here
    return tokens

# Define function to generate chat interface
def chat_interface():
    st.title("College Chatbot")
    st.markdown("Welcome! How can I assist you today?")
    user_input = st.text_input("You:")
    if st.button("Send"):
        analyzed_input = analyze_input(user_input)
        response = chatbot.respond(user_input)
        st.text_area("Chatbot:", value=response, height=100)

# Main function to run the app
if __name__ == "__main__":
    chat_interface()
