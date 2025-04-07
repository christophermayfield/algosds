#doubly linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return 

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current
    def delete(self,key):
        current = self.head 

        while current:
            if current.data == key:
                #if it is the head 
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next 
                    if current.next:
                        current.next.prev = current.prev
                return 

            current = current.next 
        print(f'{key} not found in the list')

    def print_forward(self):
            current = self.head 
            while current:
                print(current.data, end=" <-> ")
                last = current
                current = current.next 
            print("None")

    def print_backward(self):
            current = self.head 
            if not current:
                print("List is empty")
                return 
            while current.next:
                current = current.next 

            while current:
                print(current.data, end=" <-> ")
                current = current.prev


                


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

dll.print_forward()   # 10 <-> 20 <-> 30 <-> None
dll.print_backward()  # 30 <-> 20 <-> 10 <-> None

dll.delete(20)
dll.print_forward()   # 10 <-> 30 <-> None