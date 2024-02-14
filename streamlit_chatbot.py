import tkinter as tk
from tkinter import scrolledtext

class ChatBotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ChatBot")
        
        # Text area for displaying chat messages
        self.chat_display = scrolledtext.ScrolledText(self.window, width=40, height=10)
        self.chat_display.grid(column=0, row=0, padx=10, pady=10)
        
        # Text entry field for user input
        self.user_input = tk.Entry(self.window, width=40)
        self.user_input.grid(column=0, row=1, padx=10, pady=10)
        
        # Button to send user input
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.grid(column=1, row=1, padx=10, pady=10)
        
        # Bind the Enter key to send message function
        self.window.bind('<Return>', self.send_message)
        
        # Initialize chatbot response
        self.chatbot_response("Welcome to the ChatBot! How can I help you?")
        
    def start(self):
        self.window.mainloop()
        
    def send_message(self, event=None):
        user_message = self.user_input.get()
        if user_message:
            self.chat_display.insert(tk.END, "You: " + user_message + "\n")
            self.user_input.delete(0, tk.END)
            self.chatbot_response("I'm just a simple ChatBot!")
        
    def chatbot_response(self, message):
        self.chat_display.insert(tk.END, "ChatBot: " + message + "\n")
        
if __name__ == "__main__":
    chatbot_gui = ChatBotGUI()
    chatbot_gui.start()
