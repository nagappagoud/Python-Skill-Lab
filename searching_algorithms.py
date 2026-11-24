# DATA STRUCTURES AND ALGORITHMS
# Searching Algorithms
# 1. Linear Search
# 2. Binary Search


# --------------------------------
# 1. LINEAR SEARCH
# --------------------------------

print("----- LINEAR SEARCH -----")

numbers = [10, 25, 8, 40, 15]

# Element to search
search = 40

# Check each element one by one
for i in range(len(numbers)):

    # Compare current element with search element
    if numbers[i] == search:
        print("Element found at position:", i + 1)
        break

else:
    print("Element not found")


# --------------------------------
# 2. BINARY SEARCH
# --------------------------------

print("\n----- BINARY SEARCH -----")

# Binary Search requires sorted data
numbers = [8, 10, 15, 25, 40]

# Element to search
search = 40

# Initialize low and high
low = 0
high = len(numbers) - 1

# Repeat until the element is found or search ends
while low <= high:

    # Find middle position
    mid = (low + high) // 2

    # Check whether middle element is the required element
    if numbers[mid] == search:
        print("Element found at position:", mid + 1)
        break

    # Search in the right half
    elif numbers[mid] < search:
        low = mid + 1

    # Search in the left half
    else:
        high = mid - 1

else:
    print("Element not found")