# Functions are designed to do a specific job 

# You give it a name.
# You give it inputs/parameters (optional).
# It does something for you.
# You can use it again and again without rewriting the code

def greet():
    return "Hello! I'm your chatbot 🤖"

def ask_name():
    return "What's your name?"

def say_goodbye():
    return "Goodbye! Talk to you soon 👋"

def greet_player():
    print("Welcome to the game!") # this is what the function does
    

# How we call functions
greet_player()
print(greet())
print(ask_name())
print(say_goodbye())


# Different types of functions 

# A function that does stuff
# A function that returns a value 


# EXCERISES

height = int(input('what is your height? '))

def print_height():
    if height > 150:
        print('You can go on the ride')

print_height()





# Functions with parameters 

def harvest_crop(crop):
    print("You harvested:", crop)

harvest_crop("Wheat")


# functions with parameters that returns a value

def add_emeralds(current, new):
    total = current + new
    return total

total_emeralds = add_emeralds(5,10)
print(total_emeralds)



def welcome():
    print("Welcome to Minecraft!")

# Calls
welcome()
welcome()


def mine(pickaxes):
    while pickaxes > 0:
        print("Mining!")
        pickaxes -= 1
    print("All pickaxes broke!")

# Call
mine(3)

def trade(emeralds, cost):
    remaining = emeralds - cost
    return remaining

# Call
remaining_emeralds = trade(20, 7)
print("Emeralds left:", remaining_emeralds)


def square(number):
    print(number * number)

# Call
square(4)  # 16
square(7)  # 49


def apply_discount(price, discount):
    return price - (price * discount / 100)

# Call
new_price = apply_discount(100, 20)
print("Price after discount:", new_price)  # 80
