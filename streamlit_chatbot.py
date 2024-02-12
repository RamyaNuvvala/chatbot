import streamlit as st
from transformers import pipeline

# Load pre-trained model
nlp = pipeline("text-generation", model="distilgpt2")

# Define function to generate chat interface
def chat_interface():
    st.title("Chatbot with GPT-2")
    st.markdown("Welcome! How can I assist you today?")
    user_input = st.text_input("You:")
    if st.button("Send"):
        response = generate_response(user_input)
        st.text_area("Chatbot:", value=response, height=100)

# Function to generate response using pre-trained model
def generate_response(user_input):
    # Generate response using pre-trained model
    generated_response = nlp(user_input, max_length=50, do_sample=False)[0]['generated_text']
    return generated_response

# Main function to run the app
if __name__ == "__main__":
    chat_interface()
    
