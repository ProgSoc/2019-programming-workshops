# basic operators - boolean, greater/less than/equals

firstYear = False
if firstYear == True:
    print("I am a first year")
else:
    print("I am not a first year!")

# When dealing with boolean values, we can also just use the variable without using == True or == False
if firstYear:
    print("I am a first year")
else:
    print("I am not a first year!")
    
# We can compare other values such as integers
if 10 < 20:
    print("10 is less than 20!")
else:
    print "The math just doesn't add up...."

meal = "dinner"
if meal == "breakfast":
    print("Time to eat breakfast!")
elif meal == "lunch":
    print("It is lunch time")
elif meal == "dinner":
    print("I am ready for dinner")
else:
    print("I feel like a snack")
