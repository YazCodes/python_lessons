# Prices
ice_coffee = 3
hot_chocolate = 5
green_tea = 2

# Ask user for quantities
qty_ice_coffee = int(input("How many ice coffees? "))
qty_hot_chocolate = int(input("How many hot chocolates? "))
qty_green_tea = int(input("How many green teas? "))

# Calculate total
total = (ice_coffee * qty_ice_coffee) + (hot_chocolate * qty_hot_chocolate) + (green_tea * qty_green_tea)

# Show result (using f-strings)
print(f"Your total cost is: {total}")
