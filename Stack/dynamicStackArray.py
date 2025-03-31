class DynamicStackArray:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isempty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.isempty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
stack = DynamicStackArray()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.peek())
print(stack.size())