class FixedStackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def isempty(self):
        return self.top == -1
    
    def isfull(self):
        return self.top == self.capacity == -1 

    def push(self, item):
        if self.isfull():
            raise OverflowError("Stack is full")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.isempty():
            raise IndexError("Stack is empty")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item
    
    def peek(self):
        if self.isempty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]
    
    def size(self):
        return self.top + 1
    
stack = FixedStackArray(5)
stack.push(10)
stack.push(20)
print(stack.pop())
print(stack.peek())
print(stack.size())