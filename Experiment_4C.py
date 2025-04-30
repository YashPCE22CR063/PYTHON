# Creating a list
fruits = ["apple", "banana", "cherry"]

# Printing the list
print("Original List:", fruits)

# Accessing list elements (index starts at 0)
print("First fruit:", fruits[0])  # Accessing the first item
print("Second fruit:", fruits[1])  # Accessing the second item
# Adding an item to the list
fruits.append("orange")
print("List after adding 'orange':", fruits)

# Removing an item from the list
fruits.remove("banana")
print("List after removing 'banana':", fruits)

# Modifying an item in the list
fruits[1] = "kiwi"
print("List after changing second item to 'kiwi':", fruits)

# Length of the list
print("Number of fruits in the list:", len(fruits))

# Looping through the list
print("All fruits in the list:")
for fruit in fruits:
    print(fruit)
