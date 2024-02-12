import streamlit as st

# Define a dictionary of departmental links
department_links = {
    "Computer Science": "http://www.example.com/computer_science",
    "Biology": "http://www.example.com/biology",
    "Physics": "http://www.example.com/physics",
    # Add more departments and corresponding links as needed
}

# Define a dictionary of other links
other_links = {
    "College Website": "http://www.example.com",
    "Moodle": "http://moodle.example.com",
    "Notices": "http://notices.example.com",
    "Academic Calendar": "http://calendar.example.com",
    "Placements": "http://placements.example.com"
}

# Define a dictionary of predefined responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! How can I assist you?",
    "hey": "Hey! What can I do for you today?",
    "default": "I'm sorry, I don't understand. Can you please rephrase?"
}

# Function to generate response based on user input
def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if input matches any predefined responses
    if user_input in responses:
        return responses[user_input]
    
    # Check if input matches any departmental links
    elif user_input in department_links:
        return f"Here is the link to the {user_input} department: [{user_input}]({department_links[user_input]})"
    
    # Check if input matches any other links
    elif user_input in other_links:
        return f"Here is the link to {user_input}: [{user_input}]({other_links[user_input]})"
    
    else:
        return responses["default"]

# Function to save feedback to a file
def save_feedback(feedback):
    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")

# Main function to interact with the user
def main():
    st.title("College Chatbot")
    st.write("Welcome! Type your message below.")

    while True:
        # Display text input field for user input
        user_input = st.text_input("You:")

        if user_input:
            # Get bot response
            bot_response = get_response(user_input)

            # Display bot response
            st.text("Bot: " + bot_response)

            # Clear the input field after processing
            st.text_input("")

            # Check if user input is feedback
            if user_input.lower().startswith("feedback:"):
                feedback = user_input[len("feedback:"):].strip()
                save_feedback(feedback)
                st.success("Thank you for your feedback! We appreciate your input.")

# Call the main function to start the Streamlit app
if __name__ == "__main__":
    main()
