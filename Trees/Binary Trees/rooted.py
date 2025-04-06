class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data <= root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.data, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data, end=" ")

root = Node(50)

root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("In-order traversal:")
printInorder(root)

print("\nPre-order traversal:")
printPreorder(root)

print("\nPost-order traversal:")
printPostorder(root)