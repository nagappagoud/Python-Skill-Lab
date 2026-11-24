# DATA STRUCTURES AND ALGORITHMS
# SORTING ALGORITHMS

# Sorting means arranging elements in ascending or descending order.


# --------------------------------
# 1. BUBBLE SORT
# --------------------------------

print("----- BUBBLE SORT -----")

numbers = [40, 10, 25, 8, 15]

# Find the length of the list
n = len(numbers)

# Compare adjacent elements
for i in range(n):
    for j in range(0, n - i - 1):

        # Swap elements if they are in the wrong order
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Display sorted list
print("Sorted List:", numbers)


# --------------------------------
# 2. SELECTION SORT
# --------------------------------

print("\n----- SELECTION SORT -----")

numbers = [40, 10, 25, 8, 15]

# Find the length of the list
n = len(numbers)

# Find the smallest element
for i in range(n):
    min_index = i

    for j in range(i + 1, n):

        # Compare elements to find the minimum
        if numbers[j] < numbers[min_index]:
            min_index = j

    # Swap the smallest element with the current element
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Display sorted list
print("Sorted List:", numbers)


# --------------------------------
# 3. INSERTION SORT
# --------------------------------

print("\n----- INSERTION SORT -----")

numbers = [40, 10, 25, 8, 15]

# Start from the second element
for i in range(1, len(numbers)):

    # Store the current element
    key = numbers[i]

    j = i - 1

    # Move greater elements one position ahead
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1

    # Insert the element into its correct position
    numbers[j + 1] = key

# Display sorted list
print("Sorted List:", numbers)