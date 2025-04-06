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
    pass 