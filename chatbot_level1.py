import random

# Learnings - if else statement, while loops, lists, strings & functions 
# to make it harder can customise it colours, layouts etc 
# can make it customiseable to students own theme for the chatbot, minecraft related etc 

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hi there! 👋", "Hello! How are you?", "Hey hey hey! 😄"])
    elif "how are you" in user_input:
        return "I’m just a chatbot, but I’m happy to chat! 🤖"
    elif "bye" in user_input:
        return "Goodbye! Talk soon 👋"
    elif "joke" in user_input:
        return random.choice(["Why was the computer cold? It left its Windows open! 😂",
                              "What do you call a robot that loves sweets? A candy-bot 🍬"])
    else:
        return "Hmm, I don’t know what to say… 🤔 Try asking me something else!"

while True:
    user_text = input("You: ")
    if "bye" in user_text.lower():
        print("Chatbot: Goodbye! 👋")
        break
    print("Chatbot:", chatbot_response(user_text))
