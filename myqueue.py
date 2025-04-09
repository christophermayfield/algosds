#queue 

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return (len(self.items) == 0)
    

    def add(self, item):
        self.items.append(item)

    def remove(self):
        self.items.pop()

    def check_line_length(self):
        print(len(self.items))
    


myq = Queue()
myq.add(55)
myq.add(73)
myq.add(22)

print(myq.is_empty())
