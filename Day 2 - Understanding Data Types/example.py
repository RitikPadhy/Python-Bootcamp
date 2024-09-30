# Subscripting
print("Hello"[0])
print("Hello"[4])
print("Hello"[-1])

# String
print("123"+"456")

# Integer - whole numbers
print(123+345)

# Large Integers - removes the commas or underscores
print(123,456,789)
print(123456789)

# Float - floating numbers
print(3.14159)

# Boolean
print(True)
print(False)

# Len function does not work with numbers but only with strings - len(1234) - error

# type function gives us the datatype of the variable
print(type(123.45))
print(type(123))
print(type("123"))
print(type(True))

# Numbers adding
print(int("123")+int("456"))
# Error - print(int("123")+int("456")) - Cant convert string to number

# Type casting - int(), float(), str(), bool()

name_of_the_user = input("Enter your name")
length_of_the_user = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_the_user))