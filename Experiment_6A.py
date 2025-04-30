def count_characters(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1  # Increment the count if the character is already in the dictionary
        else:
            char_count[char] = 1  # Initialize the count for new characters

    return char_count

# Example usage
input_string = "hello world"
character_counts = count_characters(input_string)
print("Character counts:", character_counts)
