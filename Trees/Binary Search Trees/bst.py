class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#insert data
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

#search data
def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right, key)
    return search(root.left, key)

#delete data
def deleteNode(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Create a root node
root = None
keys = [50, 30, 70, 20, 40, 60, 80]

# Insert keys
for key in keys:
    root = insert(root, key)

# Print traversals
print("Inorder traversal:")
inorder(root)  # Should print: 20 30 40 50 60 70 80

print("\nPreorder traversal:")
preorder(root)  # Root first

print("\nPostorder traversal:")
postorder(root)  # Root last

# Search for a key
print("\n\nSearching for 60:")
found = search(root, 60)
print("Found" if found else "Not Found")

# Delete a key
print("\nDeleting 70")
root = deleteNode(root, 70)

# Print inorder again to check deletion
print("Inorder traversal after deletion:")
inorder(root)    