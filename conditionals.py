# What are Conditionals?

# Conditionals are like making choices in a story or game.
# They let the computer decide what to do based on a rule (true or false)


# if it is raining 
# then, take an umbrella
# else, leave umbrella at home

# 4 types of conditionals in Python 

# 1: if statements - checks the condition 

raining_today = False

if raining_today == True:
    print('Take an umbrella')

# 2: if else statements - gives another choice

weather = input("What’s the weather like today? (sunny/rainy): ")

if weather == "rainy":
    print("Don’t forget your umbrella! ☔")
else:
    print("Wear your sunglasses!")


lives = int(input("How many lives do you have? "))

if lives > 0:
    print("You can keep playing!")
else:
    print("Game over!")

price = int(input("How much is your shopping?"))

if price > 50:
    print("You get a 10% discount!")
else:
    print("No discount today")



# 3: if elif and else - more choices 

flavour = input("What ice cream do you want? (chocolate/vanilla): ")

if flavour == "chocolate":
    print("Yum! Chocolate is delicious!")
elif flavour == "vanilla":
    print("Classic choice!")
else:
    print("Sorry, we don’t have that flavour today")


age = int(input("How old are you? "))

if age < 13:
    print("You’re a kid!")
elif age < 18:
    print("You’re a teenager!")
else:
    print("You’re an adult!")


tool = input("Which tool are you using? (pickaxe/shovel/sword): ")

if tool == "pickaxe":
    print("You can mine stone and ores")
elif tool == "shovel":
    print("You can dig dirt and sand!")
elif tool == "sword":
    print("You can fight mobs!")
else:
    print("That tool doesn’t exist in Minecraft")

hearts = int(input("How many hearts do you have left? (0–10): "))

if hearts == 0:
    print("You died! Respawn needed")
elif hearts < 5:
    print("Careful, you’re low on health. Eat some food!")
else:
    print("You’re strong and ready to fight!")

emeralds = int(input("How many emeralds do you have? "))

if emeralds >= 20:
    print("You can buy enchanted armour!")
elif emeralds >= 10:
    print("You can buy food")
else:
    print("Not enough emeralds. Go mining! ⛏️")



# Conditionals = making choices

# Loops = repeating while a condition is true