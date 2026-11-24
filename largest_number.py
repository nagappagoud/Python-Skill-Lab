#Data Structures and Algorithms (DSA)
#Concept: Array / List Traversal
#Operation: Finding the Maximum Element
#Logic: Linear Search (comparing each element one by one).

# Program to find the largest number

numbers = [10, 25, 8, 40, 15]

# Assume the first number is the largest
largest = numbers[0]

# Check each number in the list
for num in numbers:

    # Compare the current number with the largest
    if num > largest:
        largest = num

# Print the largest number
print("Largest number is:", largest)