# Printing to the terminal
print("Hello World!")

# Variables
# You don't specify the type as Python is a dynamically typed language
a = 28 # Integer
b = 1.5 # Float
c = "Hello!" # String
d = True # Boolean
e = None # None Type

# Taking input from the user and greeting them
name = input("Enter your name: ");
print("Hello " + name); # Using Concatenation
print(f"Hello {name}"); # Using fstrings

# Conditions
num = int(input("Enter a number: "))

if num > 0:
    print("POSITIVE Number")
elif num == 0:
    print("Number is ZERO")
else:
    print("NEGATIVE Number")

# Functions
def square(x):
    return x * x
