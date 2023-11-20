import streamlit as st
import webbrowser
import re

class CollegeChatbot:
    def __init__(self):
        self.short_forms = {
            "cse": "Computer Science and Engineering",
            "ece": "Electronics and Communication Engineering",
            "eee": "Electrical and Electronics Engineering",
            'iot': "Internet of Things",
            "aiml": "Artificial Intelligence and Machine Learning",
            "it": 'Information Technology',
            'csbs': 'Computer Science and Business Systems',
            'ds': 'Data Science',
        }
        self.college_data = {
            "college_website": "http://www.collegewebsite.com",
            "moodle_link": "http://courses.rvrjc.ac.in/moodle/",
            "departments": {
                "Computer Science and Engineering": {
                    "link": "http://cse.rvrjcce.ac.in/",
                },
                # Add more departments
            },
            "academic_calendars": {
                "I Year Odd": "https://drive.google.com/file/d/1jjdp1Q_oSGkB0wgrSYZGSW33oalFQN2f/view",
                "I Year Even": "https://drive.google.com/file/d/1jjdp1Q_oSGkB0wgrSYZGSW33oalFQN2f/view",
                "II Year Odd": "https://drive.google.com/file/d/1XcXMJ5xf8h6g-GSBYnYZIHvyzqDEk6YR/view",
            }
        }

    def send_message(self, user_message):
       
        st.write(f"You: {user_message}")
        bot_response = self.get_bot_response(user_message)
        st.write(f"Chatbot: {bot_response}")
        self.open_links_in_message(bot_response)

   

    def get_bot_response(self, user_message):
        if "moodle" in user_message.lower():
            return f"Sure! You can access the college Moodle [here]({self.college_data['moodle_link']})."
        elif "college website" in user_message.lower():
            return f"Visit the college website [here]({self.college_data['college_website']})."
        elif "departments" in user_message.lower():
            return self.get_department_links()
        elif "academic calendar" in user_message.lower():
            return self.get_academic_calendar(user_message)
        else:
            department_link = self.get_department_link(user_message)
            if department_link:
                return department_link
            else:
                return "I'm sorry, I couldn't understand your query."

    def get_department_link(self, user_message):
        user_message = user_message.lower()
        for department, data in self.college_data['departments'].items():
            if department.lower() in user_message:
                return f"Here is the link for the {department} department: [Visit Department Website]({data['link']})"
        for short_form, department in self.short_forms.items():
            if short_form in user_message:
                return f"Here is the link for the {department} department: [Visit Department Website]({self.college_data['departments'][department]['link']})"
        return "I don't have information about that department."

    def get_academic_calendar(self, user_message):
        user_message = user_message.lower()
        for semester, pdf_path in self.college_data['academic_calendars'].items():
            if any(keyword in user_message for keyword in semester.lower().split()):
                return f"Here is the academic calendar for {semester}: [View Academic Calendar]({pdf_path})"
        return "I don't have the academic calendar for that semester."

    def open_links_in_message(self, message):
        links = self.extract_links(message)
        for link in links:
            st.markdown(f"[Link]({link})")

    def extract_links(self, text):
        return re.findall(r'(https?://\S+)', text)

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

if __name__ == "__main__":
    main()
