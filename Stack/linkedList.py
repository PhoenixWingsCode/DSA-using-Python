#creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.isempty():
            return None
        
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
        
    def peek(self):
        if self.isempty():
            return
        else:
            return self.head.data
        
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack underflow")
        else:
            while(iternode!=None):
                print(iternode.data, end="")
                iternode = iternode.next
                if(iternode != None):
                    print(" -> ",end="")
            return
        
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("\nTop element : ", stack.peek())

print("Popped element : ", stack.pop())
print("Popped element : ", stack.pop())

stack.display()