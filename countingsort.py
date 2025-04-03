#counting sort 
#O(n + k) - works only for positive integers
#best for small range of numbers 
#count occurances of each number
#place numberes in sorted order

def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] +=1
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
    return sorted_arr



arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)