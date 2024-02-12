import streamlit as st

class CollegeChatbot:
    def __init__(self):
        pass

    def send_message(self, user_message):
        st.write(f"You: {user_message}")
        # Logic to process user message and generate response
        bot_response = self.get_bot_response(user_message)
        st.write(f"Chatbot: {bot_response}")

    def get_bot_response(self, user_message):
        # Replace this with your actual logic to generate bot response
        return "Bot response goes here"

def main():
    st.title("College Chatbot")
    st.markdown(
        """
        #### Welcome to the College Chatbot!
        Ask me about the college website, departments, academic calendars, and more.
        """
    )
    chatbot = CollegeChatbot()

    user_input = st.text_input("You:")
    if st.button("Send"):
        chatbot.send_message(user_input)

    # Example of using text as buttons for specific selections
    st.write("Select a department:")
    if st.button("Computer Science and Engineering"):
        chatbot.send_message("Computer Science and Engineering")
    if st.button("Electronics and Communication Engineering"):
        chatbot.send_message("Electronics and Communication Engineering")
    if st.button("Electrical and Electronics Engineering"):
        chatbot.send_message("Electrical and Electronics Engineering")
    # Add more buttons for other departments

if __name__ == "__main__":
    main()
        
