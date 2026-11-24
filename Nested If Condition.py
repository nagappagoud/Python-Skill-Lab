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