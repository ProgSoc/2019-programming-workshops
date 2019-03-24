# Variables, Strings, Operators and Concatenation

name = 'Harry Potter'
age = 21
isStudent = True # Notice how 'Student' is capitalized whilst 'is' isn't? (This is called camelCasing!)
print('My name is', name)
# You can also concatenate strings with '+', but python only concatenates strings when you use the '+' symbol (and it doesn't add a space)
print('My name is ' + name)
print('I am', age, 'years old')
print('Am I a student?', isStudent)


# We can add the values of variables together
num1 = 10
num2 = 20
print("10 + 20 =", num1 + num2)
# Subtract the values
print("10 - 20 =", num1 - num2)
# Multiply the values
print("10 * 20 =", num1 * num2)
# Divide the values - left divided by right (and much more!)
print("10 / 20 =", num1 / num2)
# Modulus, gives remainder of the divided values
print("10 % 20 =", num1 % num2)

# Returns True if the two values are equal (otherwise returns False)
print("Is 10 == 20 ?", num1 == num2)
# Returns True if left is greater than right (otherwise returns False)
print("Is 10 > 20 ?", num1 > num2)
# Returns True if left is less than right (otherwise returns False)
print("Is 10 < 20 ?", num1 < num2)
# Returns True if left is greater than or equal to right (otherwise returns False)
print("Is 10 >= 20 ?", num1 >= num2)
# Returns True if left is less than or equal to right (otherwise returns False)
print("Is 10 <= 20 ?", num1 <= num2)

# TypeError: cannot concatenate 'str' and 'int' objects
# print('I am ' + age + ' years old')

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

if meal == "breakfast":
    print("Time to eat breakfast!")
elif meal == "lunch":
    print("It is lunch time")
elif meal == "dinner":
    print("I am ready for dinner")
else:
    print("I feel like a snack")

# infinite loop... be careful!
while hungry is True:
    print("Om nom nom...")

# this loop will stop after the first print
while hungry is True:
    print("Eating some pizza...")
    hungry = False

for laps in range(10):
    print("Running 10 laps... Lap number", (laps+1))

# returns the power of two numbers using the in-built pow() function
def powerOf(num1, num2):
    return pow(num1,num2)

# returns a full name, given the parameters first name and last name
def getFullName(firstName, lastName):
    return firstName + " " + lastName

#
# https://codebunk.com/b/151308735/
#
# 
# https://codebunk.com/b/474312295
# 

