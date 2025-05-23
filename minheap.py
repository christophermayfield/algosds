#min heap
#parents are less than their children 
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self,value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

        
    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        #Move last element to root and fix heap 
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val
    def peek(self):
        if not self:
            return None
        return self.heap[0]
    def _bubble_up(self,index):
        while index > 0:
            parent = (index - 1) // 2 #floor division - returns integer part of div. 
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    def _bubble_down(self,index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index 
            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

