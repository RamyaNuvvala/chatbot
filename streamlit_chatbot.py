import streamlit as st

class CollegeChatbot:
    def __init__(self):
        self.department_links = {
            "Computer Science and Engineering": "http://cse.rvrjcce.ac.in/",
            "Electronics and Communication Engineering": "http://ece.rvrjcce.ac.in/",
            "Electrical and Electronics Engineering": "http://eee.rvrjcce.ac.in/",
            # Add more department links as needed
        }

        self.other_links = {
            "College Website": "http://www.collegewebsite.com",
            "Moodle": "http://courses.rvrjc.ac.in/moodle/",
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

    # Button to select departments
    if st.button("Departments"):
        st.write("Select a department category:")
        if st.button("Select"):
            st.write("Select a department:")
            for department, link in chatbot.department_links.items():
                if st.button(department):
                    open_link(link)

    # Buttons for other links
    for name, link in chatbot.other_links.items():
        if st.button(name):
            open_link(link)

def open_link(url):
    st.markdown(f"[Open Link]({url})")

if __name__ == "__main__":
    main()
        
