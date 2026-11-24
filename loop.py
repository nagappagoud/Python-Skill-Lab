#Python loops = for loop , while loop , nested loop

#A for loop is a control statement used to repeat a block of code multiple times by iterating over a sequence such as a list, string, or range.
#-------------------------------------------------------------------------
# Program to print multiplication table

num = int(input("Enter a number: "))

# Using for loop to print table
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#A while loop is used to repeat a block of code as long as the given condition is True.
#----------------------------------------------------------------------------------

i = 1

while i <= 5:
    print(i)
    i += 1

#Nested If is a conditional statement in which an if statement is written inside another if statement.
#--------------------------------------------------------------------------

# Nested if using password verification

userid = input("Enter User ID: ")

if userid == "admin":
    
    password = input("Enter Password: ")

    if password == "12345":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid User ID")