def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be placed correctly
        j = i - 1
        
        print(f"Iteration {i}: Trying to place {key}")
        
        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(f"  Moving {arr[j]} to position {j + 1}")
            j -= 1
        
        arr[j + 1] = key  # Insert key into its correct position
        print(f"  Placed {key} at position {j + 1}")
        print(f"  Current array state: {arr}")
    
    return arr

# Example usage
array = [8, 4, 6, 2, 9]
sorted_arr = insertion_sort(array)
print("Sorted array:", sorted_arr)
