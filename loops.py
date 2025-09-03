# loops go through each item of your list 
# loops repeat the job until everything is done
# loops saves time and allows you to write less code

crops = ["wheat", "grain", "barley"]

for crop in crops:
    print("You have harvested:", crop)


# Inventory check 

inventory = ["sword", "apple", "torch"]

for item in inventory:
    print("You have a", item)


# while loops - while that condition is true, it will keep on running 

pickaxes = 3 

while pickaxes > 0:
    print("I'm mining with a pickaxe")
    pickaxes -= 1

print("No more pickaxes :(") # this is outside of the loop, so when the condition is not true anymore this will print 