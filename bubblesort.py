#bubble sort 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        #flag 
        swapped = False

        #Last i elements are already in place 
        for j in range(0,n-i-1):
            #Compare adjacent elements
            if arr[j] > arr[j+1]:
                #swap them if they're in wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr