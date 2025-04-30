# Creating a tuple
fruits_tuple = ("apple", "banana", "cherry")

# Printing the tuple
print("Original Tuple:", fruits_tuple)

# Accessing tuple elements (index starts at 0)
print("First fruit:", fruits_tuple[0])  # Accessing the first item
print("Second fruit:", fruits_tuple[1])  # Accessing the second item

# Tuple unpacking
fruit1, fruit2, fruit3 = fruits_tuple
print("Unpacked fruits:", fruit1, fruit2, fruit3)

# Checking the length of the tuple
print("Number of fruits in the tuple:", len(fruits_tuple))

# Looping through the tuple
print("All fruits in the tuple:")
for fruit in fruits_tuple:
    print(fruit)

# Nested tuples
nested_tuple = (("apple", "banana"), ("cherry", "orange"))
print("Nested Tuple:", nested_tuple)

# Accessing elements from nested tuple
print("Accessing nested tuple element:", nested_tuple[0][1])  # Output will be "banana"
