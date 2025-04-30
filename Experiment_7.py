def count_character_frequency(file_path):
    char_count = {}

    try:
        with open(file_path, 'r') as file:
            # Read the file content
            content = file.read()

            # Count the frequency of each character
            for char in content:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        return char_count

    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
file_path = input("Enter the path to the text file: ")
character_frequencies = count_character_frequency(file_path)

print("Character Frequencies:", character_frequencies)
