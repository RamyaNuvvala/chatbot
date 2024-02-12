import streamlit as st

# Function to save feedback to a text file
def save_feedback(feedback):
    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")

# Main function to interact with the user
def main():
    st.title("College Chatbot")
    st.write("Welcome! Type your message below.")

    # Initialize conversation history
    conversation_history = []

    # Display text input field for user input
    user_input = st.text_input("You:")

    if user_input:
        # Add user input to conversation history
        conversation_history.append(f"You: {user_input}")

        # Get bot response
        bot_response = get_response(user_input)
        conversation_history.append(f"Bot: {bot_response}")

        # Display conversation history
        st.text_area("Conversation History:", value="\n".join(conversation_history), height=400, readonly=True)

    # Feedback button
    if st.button("Feedback"):
        feedback = st.text_area("Please provide your feedback:", max_chars=500)
        if st.button("Submit Feedback"):
            if feedback:
                # Save feedback to a text file
                save_feedback(feedback)
                st.success("Thank you for your feedback! We appreciate your input.")
            else:
                st.warning("Please provide your feedback before submitting.")

    # Download feedback file
    st.markdown("[Download Feedback File](feedback.txt)", unsafe_allow_html=True)

# Call the main function to start the Streamlit app
if __name__ == "__main__":
    main()
        
