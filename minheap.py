#min heap

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