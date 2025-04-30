def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        
        # Find the index of the minimum element in the remaining unsorted array
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
