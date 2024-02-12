import streamlit as st

class CollegeChatbot:
    def __init__(self):
        self.college_links = {
            "College Website": "http://www.collegewebsite.com",
            "Moodle": "http://courses.rvrjc.ac.in/moodle/",
            "Computer Science and Engineering": "http://cse.rvrjcce.ac.in/",
            "Electronics and Communication Engineering": "http://ece.rvrjcce.ac.in/",
            "Electrical and Electronics Engineering": "http://eee.rvrjcce.ac.in/",
            "Placement Details": "http://www.collegewebsite.com/placement",
            "Notices": "http://www.collegewebsite.com/notices",
            "Academic Calendar": "http://www.collegewebsite.com/academic-calendar",
            # Add more links as needed
        }

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
        Ask me about the college website, Moodle, departments, placement details, notices, academic calendar, and more.
        """
    )
    chatbot = CollegeChatbot()

    user_input = st.text_input("You:")
    if st.button("Send"):
        chatbot.send_message(user_input)

    # Buttons for various links
    if st.button("College Website"):
        open_link(chatbot.college_links["College Website"])
    if st.button("Moodle"):
        open_link(chatbot.college_links["Moodle"])
    if st.button("Computer Science and Engineering"):
        open_link(chatbot.college_links["Computer Science and Engineering"])
    if st.button("Electronics and Communication Engineering"):
        open_link(chatbot.college_links["Electronics and Communication Engineering"])
    if st.button("Electrical and Electronics Engineering"):
        open_link(chatbot.college_links["Electrical and Electronics Engineering"])
    if st.button("Placement Details"):
        open_link(chatbot.college_links["Placement Details"])
    if st.button("Notices"):
        open_link(chatbot.college_links["Notices"])
    if st.button("Academic Calendar"):
        open_link(chatbot.college_links["Academic Calendar"])

def open_link(url):
    st.markdown(f"[Open Link]({url})")

if __name__ == "__main__":
    main()
        
