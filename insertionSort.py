def insertion_sort(arr):
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        current_element = arr[i]
        
        # Initialize the position for the current element
        position = i
        
        # Shift elements to the right until the correct position is found
        while position > 0 and arr[position - 1] > current_element:
            arr[position] = arr[position - 1]
            position -= 1
        
        # Insert the current element at the correct position
        arr[position] = current_element

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)
