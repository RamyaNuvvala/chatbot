import streamlit as st

# Define a dictionary of predefined responses
responses = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a great day.",
    "default": "I'm sorry, I don't understand. Can you please rephrase?"
}

# Define departmental links
department_links = {
    "Computer Science": "http://www.example.com/computer_science",
    "Biology": "http://www.example.com/biology",
    "Physics": "http://www.example.com/physics",
    # Add more departments and corresponding links as needed
}

# List of department-related keywords
department_keywords = ["department", "major", "faculty", "course"]

# Function to check if user input is related to departments
def is_department_related(user_input):
    for keyword in department_keywords:
        if keyword in user_input.lower():
            return True
    return False

# Function to generate response based on user input
def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if input matches any departmental links
    if user_input.title() in department_links:
        return f"Here is the link to the {user_input.title()} department: [{user_input.title()}]({department_links[user_input.title()]})"
    
    # Check if input is related to departments
    elif is_department_related(user_input):
        return "Select a department:"
    
    # Check if input matches any predefined responses
    elif user_input in responses:
        return responses[user_input]
    
    else:
        return responses["default"]

# Main function to interact with the user
def main():
    st.title("College Chatbot")
    st.write("You can start chatting. Type your message below.")

    # Initialize state variables
    user_input = ""
    last_user_input = ""
    show_departments = False
    
    while True:
        # Display text input field
        user_input = st.text_input("You:", value=user_input)
        
        if user_input != last_user_input:
            last_user_input = user_input
            
            # Process user input and display bot response
            bot_response = get_response(user_input)
            st.markdown(f"**Bot:** {bot_response}")
            
            # Display department selection buttons only if user asks about departments
            if bot_response == "Select a department:":
                show_departments = True
                st.write("**Departments:**")
                for department in department_links:
                    if st.button(department):
                        bot_response = get_response(department)
                        st.markdown(f"**Bot:** {bot_response}")
            else:
                show_departments = False
        
        # Hide department selection buttons if a department is selected
        if not show_departments:
            st.write("")

# Call the main function to start the Streamlit app
if __name__ == "__main__":
    main()
        
