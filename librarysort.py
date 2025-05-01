#library sort 
#works similarly to insertion sort but adds gaps to reduce the cost of shifting
#elements 

import math 

def library_sort(arr, epsilon = 1):
    if not arr:
        return []
    
    n = len(arr)
    size = int((1 + epsilon) * n)
    shelf = [None] * size  # Create a shelf with gaps
    num_elements = 0

    def find_insert_position(val):
        # Binary search to find the correct insert position
        low, high = 0, size - 1
        while low <= high:
            mid = (low + high) // 2
            if shelf[mid] is None:
                # Search neighbors
                left, right = mid - 1, mid + 1
                while True:
                    if left < low and right > high:
                        mid = right
                        break
                    if left >= low and shelf[left] is not None:
                        mid = left
                        break
                    if right <= high and shelf[right] is not None:
                        mid = right
                        break
                    left -= 1
                    right += 1
            if shelf[mid] is None or shelf[mid] > val:
                high = mid - 1
            else:
                low = mid + 1
        return low

    for value in arr:
        pos = find_insert_position(value)
        # Shift right to make space if needed
        while pos < size and shelf[pos] is not None:
            pos += 1
        if pos >= size:
            # Rebalance the shelf
            new_size = int((1 + epsilon) * (num_elements + 1))
            new_shelf = [None] * new_size
            idx = 0
            for item in shelf:
                if item is not None:
                    idx += 1  # Leave a gap
                    new_shelf[idx] = item
                    idx += 1
            shelf = new_shelf
            size = new_size
            pos = find_insert_position(value)
            while pos < size and shelf[pos] is not None:
                pos += 1
        shelf[pos] = value
        num_elements += 1

    # Filter out gaps (None values)
    return [x for x in shelf if x is not None]

# Example usage
arr = [7, 3, 1, 9, 4, 8]
sorted_arr = library_sort(arr)
print(sorted_arr)

hi = 44

