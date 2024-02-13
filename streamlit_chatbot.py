import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot("MyChatBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train("chatterbot.corpus.english")

# Function to get response from the chatbot
def get_response(user_input):
    return chatbot.get_response(user_input)

# Streamlit app
def main():
    st.title("ChatterBot Chatbot")

    user_input = st.text_input("You:", "")
    if st.button("Send"):
        if user_input:
            bot_response = get_response(user_input)
            st.write(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
    
