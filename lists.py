# Lists are able to store many items in one place 

# List = Chest in Minecraft
# append() = Add new item to chest
# remove() = Take item out
# count() = Count how many of the same item
# loop = Check every item in chest one by one

inventory = ["pickaxe", "sword", "apple"]

print("Your inventory:", inventory)
print("First item:", inventory[0])  # Which item is first?
print("Last item:", inventory[-1])  # Which item is last?

# Task: Add "torch" to the list and print the inventory.

inventory.append("torch")
inventory.append("bread")

print(inventory)

# Task: remove "apple" to the list and print the the inventory.

inventory.remove("apple")
print("Inventory after eating:", inventory)


# Task: Add another tourch to the inventory and print the inventory 

inventory.append('torch')
inventory.append('torch')
inventory.append('torch')

print(inventory)

# can also use the extend()

inventory.extend(["apple", "apple", "apple"])
print(inventory)

# counting items in inventory using count()

print("How many torches?", inventory.count("torch"))
print("How many apples?", inventory.count("apples"))

# Using min and max in lists

emeralds = [1, 5, 10, 20]

print("Emerald values:", emeralds)
print("Biggest trade:", max(emeralds))
print("Smallest trade:", min(emeralds))
