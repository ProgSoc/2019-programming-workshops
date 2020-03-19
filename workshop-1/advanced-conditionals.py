# advanced conditionals - testing multiple comparative conditionals

# we can even use 'and' and 'or' in our if, elif to test multiple conditions at the same time
vehicle = "motorbike"
brand = "Toyota"

if vehicle == "car" and (brand == "Toyota" or brand == "Subaru"):
    print("You're driving a Japanese car")
elif vehicle == "car" and (brand == "Hyundai" or brand == "Kia"):
    print("You're driving a Korean car")


if vehicle != "motorbike" and brand == "Mercedes":
    if vehicle == "truck":
        print("You're driving a German truck")
    elif vehicle == "car":
        print("You're driving a German car")

# ACTIVITY TIME!! :) (5-15 min depending on skill level)

# try to finish off my function...
print("I can't figure out how to check where the groceries should go!")
# given this list of groceries:
groceries = ["cereal", "milk", "beef steak", "ice cream", "detergent"]

# for reference, cereal = room temperature, milk = cold, beef steak = cold, ice cream = freezing, detergent = other
# remember that milk and eggs can't go with the beef steaks, and detergent should have it's own storage
# bonus points for printing this out too!!!

# create a set of if/elif/else statements that print() the type of grocery and storage location of each item!
# you can print the storage location based on their storageTemp (room temperature, cold, freezing, other)
# the most efficient statement will have less lines (logic) and be easily readable, GOOD LUCK!
