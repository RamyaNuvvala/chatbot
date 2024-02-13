import streamlit as st

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hi" in user_input:
        return "Hello!"
    elif "how are you" in user_input:
        return "I'm doing well, thank you!"
    elif "college" in user_input:
        return "Our college offers a variety of programs. What specific information are you looking for?"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    st.title("College Information Chatbot")
    st.markdown("Welcome to our college chatbot! Ask me anything about our college.")

    user_input = st.text_input("You:", "")
    if st.button("Send"):
        if user_input:
            bot_response = chatbot_response(user_input)
            st.write(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
            
