# Python Collections: List, Tuple, Set and Dictionary


# 1. LIST
# List stores multiple values.
# It allows duplicate values and can be changed.

print("----- LIST -----")

my_list = [10, 20, 30, 40, 20]

print("List:", my_list)

# Adding an element to the list
my_list.append(50)
print("After adding:", my_list)

# Removing an element from the list
my_list.remove(20)
print("After removing:", my_list)


# 2. TUPLE
# Tuple stores multiple values.
# It allows duplicates but cannot be changed.

print("\n----- TUPLE -----")

my_tuple = (10, 20, 30, 40, 20)

print("Tuple:", my_tuple)

# Accessing an element using its index
print("First element:", my_tuple[0])


# 3. SET
# Set stores unique values.
# It does not allow duplicate values.

print("\n----- SET -----")

my_set = {10, 20, 30, 40, 20}

print("Set:", my_set)

# Adding an element to the set
my_set.add(50)
print("After adding:", my_set)

# Removing an element from the set
my_set.remove(20)
print("After removing:", my_set)


# 4. DICTIONARY
# Dictionary stores data in key-value pairs.

print("\n----- DICTIONARY -----")

my_dict = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", my_dict)

# Accessing a value using its key
print("Name:", my_dict["name"])

# Adding a new key-value pair
my_dict["city"] = "Bangalore"
print("After adding:", my_dict)

# Updating an existing value
my_dict["age"] = 21
print("After updating:", my_dict)