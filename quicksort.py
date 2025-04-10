#quick sort, O(nlogn) average, O(n^2) worst case
#pick a pivot element, partition the array such that elements < pivot go left
#elements > pivot go right 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[len(arr)// 2] #picking the middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))    

