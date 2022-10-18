class Stack:

    def __init__(self):
        self.items = []

    def add(self, element):
        self.items.append(element)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("Stack is empty")

    def top(self):
     return self.items[-1]   
        
        