def are_strings_nearly_equal(s1, s2, max_length_difference=1):
    # Calculate the absolute difference in lengths
    length_difference = abs(len(s1) - len(s2))
    
    # Check if the length difference is within the allowed threshold
    return length_difference <= max_length_difference

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_strings_nearly_equal(string1, string2):
    print("The strings are nearly equal.")
else:
    print("The strings are not nearly equal.")
