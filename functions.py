# =====================================================
# FIRST-CLASS FUNCTIONS
# A function can be stored in a variable and used later.
# =====================================================

# Defining a function
def display(text):
    return text.upper()


print("FIRST-CLASS FUNCTION")

# Calling the function directly
print(display("Hello"))

# Storing a function in a variable
displayfunc = display

# Calling the function using the variable
print(displayfunc("Hello"))


# =====================================================
# HIGHER-ORDER FUNCTIONS
# A function can be passed as an argument to another function.
# =====================================================

# Defining a function to convert text into uppercase
def displayupper(text):
    return text.upper()


# Defining a function to convert text into lowercase
def displaylower(text):
    return text.lower()


# Defining a higher-order function
# It accepts another function as an argument
def displayfinal(func):
    result = func("Hi, I am created by a function")
    print(result)


print("\nHIGHER-ORDER FUNCTION")

# Passing displayupper function as an argument
displayfinal(displayupper)

# Passing displaylower function as an argument
displayfinal(displaylower)