def radix_sort(arr):
    #step 1 - Find the max number to know number of digits 
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1 #we will start with the 1s place 

    #step 2 - loop until we have processed all digit places 
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp*=10
    return arr 

def counting_sort_exp(arr,exp):
    #This function will be sorted based on digit at exp place 
    n = len(arr)
    output = [0] * n #final sorted array (by current digits)
    count = [0] * 10 #count for each digit [0-9]

    #step 1 count occurances of digits at exp place 
    for i in range(n):
        index = (arr[i] // exp) % 10 
        count[index]+=1

    #step 2 make counts cumulative (so we know the positions)
    for i in range(1,10):
        count[i] += count[i-1]

    
    #step 3: build output array (go in reverse for stability)
    for i in range(n-1,-1,-1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_exp(arr,exp)
        exp*=10
    return arr


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print('sorted arr', arr)
