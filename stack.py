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
        
    
    