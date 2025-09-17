# this is a grader that asks for a students grade 

#welcome message and input for the user 
print("Hello, welcome to your grade calculator! ")
grade = input("Please enter your grade: ") 
grade_no = float(grade)

# These are the grade conditions 
if grade_no >= 80:
    print("A")
elif grade_no >= 70:
    print("B")
elif grade_no >= 60:
    print("C")
elif grade_no >= 50:
    print("Pass ")     
elif grade_no >= 40:
    print("You have a clear pass ")

# addition of ternary operator within the if chain.
else: 
   grade_no = print("Refferal - see HOD") if grade_no >=20 else print("Fail")
 


