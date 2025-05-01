#library sort 
#works similarly to insertion sort but adds gaps to reduce the cost of shifting
#elements 

import math 

def library_sort(arr, epsilon = 1):
    if not arr:
        return []
    
