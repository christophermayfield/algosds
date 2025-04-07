#bucket sort
def insertion_sort(arr):
    #insertion sort helper algorithm 
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 


def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    #minimum and maximum values in the array 
    min_value = min(arr)
    max_value = max(arr)
    
    #number of buckets (can be adjusted)
    bucket_count = len(arr)

    #create empty buckets 
    buckets  = [[] for _ in range(bucket_count)]

    #map input array elements to corresponding buckets 
    for num in arr:
        index = int((num-min_value) / (max_value - min_value) * (bucket_count - 1))
        buckets[index].append(num)

    #sort each bucket and concatenate the results 
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)
    return sorted_arr


#usage
arr = [0.42, 0.32, 0.56, 0.21, 0.12, 0.34, 0.99]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)



