import streamlit as st
from flask import Flask, request, jsonify
import requests
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Function to respond to user input
def college_chatbot(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "courses": "We offer a variety of courses including Computer Science, Engineering, Business, and more. Which one are you interested in?",
        "admissions": "For admissions information, please visit our website or contact our admissions office.",
        "facilities": "We have state-of-the-art facilities including labs, libraries, and recreational areas. Is there anything specific you'd like to know about?",
        "default": "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"
    }
    return responses.get(user_input.lower(), responses["default"])

# Define Flask route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = college_chatbot(user_input)
    return jsonify({"response": response})

def run_flask():
    app.run(debug=False, host="localhost", port=5000)

# Streamlit app layout
def main():
    st.title("College Chatbot")

    user_input = st.text_input("You:")
    if st.button("Ask"):
        response = send_request(user_input)
        st.write(f"College Chatbot: {response}")

# Function to send request to Flask backend
def send_request(user_input):
    url = "http://localhost:5000/chat"
    data = {"user_input": user_input}
    response = requests.post(url, data=data)
    return response.json()["response"]

if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    main()
    
