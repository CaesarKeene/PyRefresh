# this is a grader that asks for a students grade 

print("Hello, welcome to your grade calculator! ")
grade = input("Please enter your grade: ") 
grade_no = int(grade) 

if grade_no >= 80:
    print("A")
elif grade_no >= 70:
    print("B")
elif grade_no >= 60:
    print("C")
elif grade_no >= 50:
    print("You have a clear pass ") 

grade_no = print("You have a referral, kindly see the HOD! ") if grade_no >= 40 else print("Fail")



