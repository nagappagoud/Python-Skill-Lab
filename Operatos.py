#Operators are special symbols or keywords used to perform operations on variables and values.
#----------------------------------------------------------------

# Shopping Bill Calculator

# Get product details
name = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))

# Arithmetic Operators
total = price * quantity

print("\n----- SHOPPING BILL -----")
print("Product Name:", name)
print("Product Price:", price)
print("Quantity:", quantity)
print("Total Amount:", total)

# Comparison Operators
print("\n----- COMPARISON OPERATORS -----")
print("Is total greater than 1000?", total > 1000)
print("Is total equal to 1000?", total == 1000)
print("Is total less than 1000?", total < 1000)

# Logical Operators
print("\n----- LOGICAL OPERATORS -----")
print("AND:", total > 500 and quantity > 1)
print("OR:", total > 1000 or quantity > 5)
print("NOT:", not(total > 1000))

# Assignment Operators
print("\n----- ASSIGNMENT OPERATORS -----")
total += 100
print("After Adding 100:", total)

total -= 50
print("After Subtracting 50:", total)

total *= 2
print("After Multiplication:", total)

total /= 2
print("After Division:", total)

# Final Bill
print("\nFinal Shopping Bill:", total)