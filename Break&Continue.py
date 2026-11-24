#Break: The break statement is used to stop the loop immediately.
#Continue: The continue statement is used to skip the current iteration and move to the next iteration of the loop.
#----------------------------------------------------------------------------------------

# Program to demonstrate break and continue statements

for i in range(1, 11):

    # Break statement: Stops the loop when i is 5
    if i == 5:
        break

    print(i)

print("Loop stopped using break")

for i in range(1, 11):

    # Continue statement: Skips 5 and continues the loop
    if i == 5:
        continue

    print(i)