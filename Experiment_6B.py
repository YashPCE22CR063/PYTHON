# Dictionary to store birthdays
birthdays = {
    "Alice": "1995-05-16",
    "Bob": "1988-11-23",
    "Charlie": "2000-01-02"
}

# Ask the user for a name
name = input("Enter the name of the person to find their birthday: ")

# Check if name exists in the dictionary
if name in birthdays:
    # Use split to break the date into parts
    date_parts = birthdays[name].split("-")
    # Format the date nicely using join
    formatted_date = "/".join(date_parts)
    print(f"{name}'s birthday is on: {formatted_date}")
else:
    print(f"No birthday record found for {name}.")
