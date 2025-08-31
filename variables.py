# Variable lesson 


# What is a variable? - where you store data

name = 'Yasmin'
favourite_number = 2; 
# What is the different between the name and favourite number variable?

# Different data types. Boolean, interger, string, floats

sunny = True
snowing = False 
movie_rating = 8.5 

int("5") # type casting


# How to print your variable 
print(name)

# EXERCISE 1
# Create a variable called my_name and store your name in it
# Then print "Hello, my name is ___"

my_name = ' Yasmin'
print('Hello my name is ', my_name)


# EXERCISE 2 
# Create a variable favourite_number1 and store your favourite number
# Print: "My favourite number is ___"

favourite_number1 = 10
print('My favourite number is ', favourite_number1 )


# EXERCISE 3
# Create two variables a and b
# Assign any numbers to them
# Swap their values (so a gets b’s value, and b gets a’s value)

a = 68
b = 39

a, b = b, a

print(a,b)


# EXC 2
# Create a variable celsius = 25
# Convert it to Fahrenheit using (celsius * 9/5) + 32
# Print the result

celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)


# EX 3 Bank account
# Start with balance = 100
# Deposit 50, then withdraw 20 (using variables)
# Print the final balance

balance = 100
balance = balance + 50
balance = balance - 20 

print(balance)


# Create variables for the prices of 3 items
# Add them up to get the total
# Print: "The total cost is: ___"

ice_coffee = 3
hot_chocolate = 5
green_tea = 2

total = ice_coffee + hot_chocolate + green_tea

print('Your total cost is:' , total)
print(f"Your total cost is: {total}")


