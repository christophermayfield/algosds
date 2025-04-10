#max heap 
#parents are greater than their children 

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._heapify_down(0)
        return max_value

    

    def __str__(self):
        return str(self.heap)


# Example usage
if __name__ == "__main__":
    heap = MaxHeap()
    elements = [15, 10, 20, 17, 8]

    for el in elements:
        heap.insert(el)
        print(f"Inserted {el}: {heap}")

    print(f"Max: {heap.extract_max()}")
    print(f"After extract: {heap}")