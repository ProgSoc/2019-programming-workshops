# Variables, Strings, Basic Addition and Concatenation

name = 'Harry Potter'
age = 21
isStudent = True # Notice how 'Student' is capitalized whilst 'is' isn't? (This is called camelCasing!)
print('My name is ' + name)
print('I am ' + str(age) + ' years old')
print('Am i a student? ' + str(isStudent))
print 'Am i a student?', str(isStudent)


# We can add the values of variables together
num1 = 10
num2 = 20
print(num1 + num2)

# We can also add strings together
firstName = "Harry"
lastName = "Potter"
fullName = firstName + lastName
print fullName

# We can re-assign values to our variables
myFavouriteNumber = 9
myFavouriteNumber = 5
print myFavouriteNumber

# TypeError: cannot concatenate 'str' and 'int' objects
# print('I am ' + age + ' years old')

