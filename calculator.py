"""
#calculator using int function for whole numbers

num1 = input("Enter a number: ") 
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result) 

"""

"""
#calculator using float function for decimal numbers
num1 = input("Enter a number: ") 
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)  
"""

# VAT rate calculation
price = input("Enter price of product (Ksh): ")
tax = input("Enter VAT percentage (%): ")

VAT_amount = int(price) * float(tax) 
final_amount = VAT_amount + int(price)
print(final_amount)





