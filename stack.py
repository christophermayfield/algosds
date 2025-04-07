class Stack:
    #create the stack
    def __init__(self):
        self.items = []
    #returns true if the stack is empty, false otherwise
    def is_empty(self):
        return len(self.item) == 0 
    
    def push(self,item):
        self.items.append(item)
        print(f'Pushed{item} to the stack')
    
    def pop(self):
        if self.is_empty():
            raise  IndexError("Pop from an empty stack")
        item = self.items.pop()
        print(f'Popped {item} from the stack')

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return f"stack: {self.items}"
    
    
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack)
    print(f"Top item is: {stack.peek()}")
    stack.pop()
    print(stack)
    print(f"Is stack empty? {stack.is_empty()}")