#single linked list 
#insert at head O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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
    
    def print_list(self):
        current = self.head 
        while current:
            print(current.data, end=' -> ')
            current = current.next 
        print("None")
    
    def delete(self,key):
        current = self.head
        prev = None
        
        #if the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            return 
        
        #search for the node to be deleted 
        while current and current.data!= key:
            prev = current
            current = current.next

        #if key was not found 
        if not current:
            print(f'{key} was not found in this list.')
            return 
        
        #unlink the node from the list
        prev.next = current.next
    def print_list(self):
        current = self.head
        while current:
            print(current.data,end=' -> ')
            current = current.next

        print("None")

#example usage
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()  # 10 -> 20 -> 30 -> None