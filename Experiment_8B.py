def compute_file_metrics(file_path):
    try:
        with open(file_path, 'r') as file:
            # Initialize counters
            num_lines = 0
            num_words = 0
            num_chars = 0
            
            # Read each line in the file
            for line in file:
                num_lines += 1  # Increment line count
                num_chars += len(line)  # Count characters in the line
                num_words += len(line.split())  # Count words in the line

        return num_lines, num_words, num_chars
file_path = "sample.txt"
compute_file_metrics(file_path)
