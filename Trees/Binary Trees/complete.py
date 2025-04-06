#checking if a binary tree is a complete binary tree in python

class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

#Count the number of nodes:
def countNodes(root):
    if root is None:
        return 0
    return (1 + countNodes(root.left) + countNodes(root.right))

#Checking if the tree is complete/perfect binary tree
def isComplete(root, index, numberNodes):
    # Check if the tree is empty
    if root is None:
        return True

    if index >= numberNodes:
        return False

    return (isComplete(root.left, 2 * index + 1, numberNodes)
            and isComplete(root.right, 2 * index + 2, numberNodes))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = countNodes(root)
index = 0

if isComplete(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")