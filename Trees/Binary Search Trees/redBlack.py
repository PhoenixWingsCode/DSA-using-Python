class Node:
    def __init__(self, data, color='red'):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color='black')
        self.root = self.NIL

    def insert(self, data):
        newNode = Node(data)
        newNode.left = self.NIL
        newNode.right = self.NIL

        parent = None
        curr = self.root

        while curr != self.NIL:
            parent = curr
            if newNode.data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        newNode.parent = parent
        if parent is None:
            self.root = newNode
        elif newNode.data < parent.data:
            parent.left = newNode
        else:
            parent.right = newNode

        newNode.color = 'red'
        self.fixInsert(newNode)

    def fixInsert(self, k):
        while k!= self.root and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.leftRotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rightRotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rightRotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.leftRotate(k.parent.parent)
        self.root.color = 'black'

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, data):
        node = self.search(self.root, data)
        if node == self.NIL:
            print("Node not found!")
            return

        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == 'black':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == 'black' and s.left.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def search(self, node, key):
        if node == self.NIL or key == node.data:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            print(f"{node.data} ({node.color})", end=" ")
            self.inorder(node.right)

# === Example usage ===
rbt = RedBlackTree()
for value in [10, 20, 30, 15, 25, 5]:
    rbt.insert(value)

print("Inorder traversal after insertion:")
rbt.inorder(rbt.root)

print("\n\nDeleting 15...")
rbt.delete(15)
print("Inorder traversal after deletion:")
rbt.inorder(rbt.root)