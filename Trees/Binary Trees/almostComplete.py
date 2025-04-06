class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# Count the number of nodes
def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

# Check if tree is complete
def isComplete(root, index, numberNodes):
    if root is None:
        return True
    if index >= numberNodes:
        return False
    return (isComplete(root.left, 2 * index + 1, numberNodes)
            and isComplete(root.right, 2 * index + 2, numberNodes))

# Build an almost complete binary tree without using lists or queues
# Here's an example with 6 nodes (complete till level 2, missing one node on level 3)
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)   # No right child for node 3, so the tree is almost complete

# Check
node_count = countNodes(root)
index = 0

if isComplete(root, index, node_count):
    print("The tree is almost complete binary tree")
else:
    print("The tree is NOT a complete binary tree")
