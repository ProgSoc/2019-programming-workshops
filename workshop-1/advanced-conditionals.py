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
