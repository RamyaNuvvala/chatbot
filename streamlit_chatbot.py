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

# Function to generate response based on user input
def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if input matches any departmental links
    if user_input.title() in department_links:
        return f"Here is the link to the {user_input.title()} department: [{user_input.title()}]({department_links[user_input.title()]})"
    
    # Check if input matches any predefined responses
    elif user_input in responses:
        return responses[user_input]
    
    else:
        return responses["default"]

# Main function to interact with the user
def main():
    st.title("College Chatbot")
    st.write("You can start chatting. Type your message below.")

    user_input = st.text_input("You:")
    if user_input:
        bot_response = get_response(user_input)
        st.markdown(f"Bot: {bot_response}")
        
        # Create department selection buttons
        st.write("Select a department:")
        for department in department_links:
            if st.button(department):
                bot_response = get_response(department)
                st.markdown(f"Bot: {bot_response}")

# Call the main function to start the Streamlit app
if __name__ == "__main__":
    main()
