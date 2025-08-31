# Classes are the blueprint of an object
# You can have many different types of chatbots with similar behaviour 
# Here it's telling us what the chatbot can do greet, ask questions and say goodbye

class Chatbot:
    def __init__(self, name):
        self.name = name  # each chatbot has a name

    def greet(self):
        return f"Hello! I'm {self.name}, your chatbot"

    def fave_colour_question(self, question):
        return f"You asked: {question}. I love pink!!"

    def say_goodbye(self):
        return f"Goodbye from {self.name}! 👋"


# Make a chatbot object
my_bot = Chatbot("Chatter")

# Use chatbot functions 
print(my_bot.greet())
print(my_bot.fave_colour_question("What's your favourite colour? "))
print(my_bot.say_goodbye())
