import streamlit as st
import webbrowser

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

    # Dictionary mapping department names to their respective links
    department_links = {
        "Computer Science and Engineering": "http://cse.rvrjcce.ac.in/",
        "Electronics and Communication Engineering": "http://ece.rvrjcce.ac.in/",
        "Electrical and Electronics Engineering": "http://eee.rvrjcce.ac.in/",
        # Add more departments and links as needed
    }

    # Button for departments label
    if st.button("Departments"):
        st.write("Select a department:")
        # Scroll-down selection for departments
        selected_department = st.selectbox("", list(department_links.keys()))
        if st.button("Open Department Link"):
            st.write(f"Opening link for {selected_department}:")
            webbrowser.open_new_tab(department_links[selected_department])

if __name__ == "__main__":
    main()
        
