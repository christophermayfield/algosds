#heapsort using heapq for simplicity 
import heapq
def heap_sort(arr):
    a = arr.copy()
    heapq.heapify(a)
    return [heapq.heappop(a) for _ in range(len(a))]

arr = [4, 2, 2, 8, 3, 3, 1]
print(heap_sort(arr))
