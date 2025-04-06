class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

def newNode(data):
    return Node(data)

#Left skewed Tree
root = newNode(1)
root.left = newNode(2)
root.left.left = newNode(3)

# The tree looks like this:
# 1
# /
# 2
# /
# 3

rightRoot = newNode(1)
rightRoot.right = newNode(2)
rightRoot.right.right = newNode(3)

# The tree looks like this:
# 1
# \
# 2
# \
# 3