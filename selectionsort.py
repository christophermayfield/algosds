#selection sort 
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        
        print(f"Iteration {i + 1}: Finding the smallest element from index {i} to {n - 1}")
        
        for j in range(i + 1, n):
            print(f"  Comparing {arr[j]} with {arr[min_index]}")
            if arr[j] < arr[min_index]:
                print(f"    {arr[j]} is smaller than {arr[min_index]}, updating min_index to {j}")
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the found minimum element with the first element
        print(f"  Swapped {arr[i]} with {arr[min_index]}")
        print(f"  Current array state: {arr}")
    
    return arr

# Example usage
arr = [8, 4, 6, 2, 9]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
