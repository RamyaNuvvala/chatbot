import streamlit as st

class CollegeChatbot:
    def __init__(self):
        pass

    def send_message(self, user_message):
        st.write(f"You: {user_message}")
        bot_response = self.get_bot_response(user_message)
        st.write(f"Chatbot: {bot_response}")

    def get_bot_response(self, user_message):
        # Welcome message
        return "Hello! Welcome to the College Chatbot. How can I assist you today?"

def main():
    st.title("College Chatbot")
    chatbot = CollegeChatbot()
    # Display welcoming message automatically when the chatbot is loaded
    st.write("Hello! Welcome to the College Chatbot. How can I assist you today?")

    user_input = st.text_input("You:")
    if st.button("Send"):
        chatbot.send_message(user_input)

if __name__ == "__main__":
    main()
    
