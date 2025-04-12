class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    #Get height of the node
    def getHeight(self, root):
        return 0 if not root else root.height
    
    #Get Balance factor
    def getBalance(self, root):
        return 0 if not root else self.getHeight(root.left) - self.getHeight(root.right)
    
    # Right rotate
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    # Left rotate
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    # Insertion
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Balance cases
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Find minimum value node
    def getMinValueNode(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # Deletion
    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Balance cases
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Search
    def search(self, root, key):
        if not root or root.key == key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# ---- Usage Example ----
avl = AVLTree()
root = None

# Insert nodes
for key in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, key)

print("Inorder traversal after insertions:")
avl.inorder(root)

# Search for a node
print("\nSearching for 25:")
print("Found" if avl.search(root, 25) else "Not Found")

# Delete a node
root = avl.delete(root, 20)
print("Inorder traversal after deleting 20:")
avl.inorder(root)