import PySimpleGUI as sg
import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "college": ["Our college offers a variety of programs. What specific information are you looking for?"],
    # Add more responses as needed
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    sg.theme("LightGrey1")

    layout = [
        [sg.Text("College Information Chatbot", font=("Helvetica", 16))],
        [sg.Output(size=(60, 20), font=("Helvetica", 12))],
        [sg.InputText(key="-INPUT-", font=("Helvetica", 12)), sg.Button("Send", font=("Helvetica", 12))]
    ]

    window = sg.Window("Chatbot", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "Send":
            user_input = values["-INPUT-"]
            if user_input:
                bot_response = chatbot_response(user_input)
                print(f"You: {user_input}")
                print(f"Bot: {bot_response}")
                print("")

    window.close()

if __name__ == "__main__":
    main()
    
