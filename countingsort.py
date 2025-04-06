#counting sort 
#O(n + k) - works only for positive integers
#best for small range of numbers 
#count occurances of each number
#place numberes in sorted order

def counting_sort(arr):
    if not arr:
        return []
    
    # Step 1: Find the maximum value in the array
    max_val = max(arr)
    
    # Step 2: Create and populate the count array
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    print(count)
    
    # Step 3: Modify the count array to store positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Step 4: Build the sorted output array
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)