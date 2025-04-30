with open(file_path, 'r') as file:
            # Read each line in the file
            for line in file:
                # Strip newline characters and reverse the line
                reversed_line = line.strip()[::-1]
                print(reversed_line)
