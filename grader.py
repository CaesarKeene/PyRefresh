# this is a grader that asks for a students grade 

#welcome message and input for the user 
print("Hello, welcome to your grade calculator! ")
grade = input("Please enter your grade: ") 
grade_no = int(grade) 

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
elif grade_no >= 20:
    print("Refferal - see HOD")

else: 
    print("Fail")   
 


