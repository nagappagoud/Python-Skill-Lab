#If-Elif-Else is a conditional statement used to check multiple conditions and execute the block of code whose condition is True.
#-----------------------------------------------------------------------------------------------------

# Student marks and grades

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")