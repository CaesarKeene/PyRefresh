"""

# Variables and Syntax 
message = 'Hello, World!'
#print(message)

message = 'Good Bye!'
#print(message) 

variable_name = 'caesar' 
character_age = '25'
print(variable_name + ' wanted to learn how to code again')
print('he is ' + character_age + " years of age now.") 

# concatenate 
new_message = message + variable_name
print(new_message)  

# Strings 

# A string with double quotes should use single quotes 
another_message = '"We are on day 2 today" he said.'
print(another_message)

# multiline string
help_message = ''' 
Password is wrong!
Hint: dog's name 
''' 
print(help_message)

# Numbers: integers 
x = 20
y = 3

total = x + y
print(total)

difference = x - y
print(difference)

product = x * y
print(product)

# quotient in python gets the remainder of the two numbers being divided
quotient = x / y
print(quotient)

# The Power of a number or exponents
a = 4 
c = 4 
power = a**c
print(power)


# Numbers: floats 
# Floats are any number that have a decimal point 

x = 0.5
y = 0.25

total = x + y
print(total)

difference = x - y
print(difference)

product = x * y
print(product)

# To make large numbers more readable you use underscores
huge_number = 10_000_000_000
print(huge_number) 

# Boolean (True or False)
x = 20
y = 3
result = x < y 
print(result) 


""" 

#Python Arithmetic Operators
#Modulus %
""" Modulus operator allows you to return the remainder of two numbers that are divided """
"""
a = 171 
if a % 1 == 1: 
    print(f"{a} is an even number")
else:  
    print(f"{a} is an odd number") 

"""
# if/else statements 
age = input("Enter your age: ")
if int(age) >= 18:
    print("You are eligible to vote")
else: 
    print("You are not eligible to vote ") 
