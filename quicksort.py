#quick sort, O(nlogn) average, O(n^2) worst case
#pick a pivot element, partition the array such that elements < pivot go left
#elements > pivot go right 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr 