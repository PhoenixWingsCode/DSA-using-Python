class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.keys = []
        self.children = []
        self.leaf = leaf

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1

        if i < len(self.keys) and self.keys[i] == key:
            return self

        if self.leaf:
            return None
        return self.children[i].search(key)

    def insert_non_full(self, key):
        i = len(self.keys) - 1

        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)

        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:t - 1]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    def delete(self, key):
        idx = self.find_key(key)

        if idx < len(self.keys) and self.keys[idx] == key:
            if self.leaf:
                self.keys.pop(idx)
            else:
                self.delete_internal_node(key, idx)
        else:
            if self.leaf:
                return  # Key not found
            flag = idx == len(self.keys)
            if len(self.children[idx].keys) < self.t:
                self.fill(idx)
            if flag and idx > len(self.keys):
                self.children[idx - 1].delete(key)
            else:
                self.children[idx].delete(key)

    def delete_internal_node(self, key, idx):
        k = self.keys[idx]
        if len(self.children[idx].keys) >= self.t:
            pred = self.get_pred(idx)
            self.keys[idx] = pred
            self.children[idx].delete(pred)
        elif len(self.children[idx + 1].keys) >= self.t:
            succ = self.get_succ(idx)
            self.keys[idx] = succ
            self.children[idx + 1].delete(succ)
        else:
            self.merge(idx)
            self.children[idx].delete(k)

    def get_pred(self, idx):
        cur = self.children[idx]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def get_succ(self, idx):
        cur = self.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def fill(self, idx):
        if idx != 0 and len(self.children[idx - 1].keys) >= self.t:
            self.borrow_from_prev(idx)
        elif idx != len(self.keys) and len(self.children[idx + 1].keys) >= self.t:
            self.borrow_from_next(idx)
        else:
            if idx != len(self.keys):
                self.merge(idx)
            else:
                self.merge(idx - 1)

    def borrow_from_prev(self, idx):
        child = self.children[idx]
        sibling = self.children[idx - 1]

        child.keys.insert(0, self.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        self.keys[idx - 1] = sibling.keys.pop()

    def borrow_from_next(self, idx):
        child = self.children[idx]
        sibling = self.children[idx + 1]

        child.keys.append(self.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        self.keys[idx] = sibling.keys.pop(0)

    def merge(self, idx):
        child = self.children[idx]
        sibling = self.children[idx + 1]

        child.keys.append(self.keys[idx])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)

        self.keys.pop(idx)
        self.children.pop(idx + 1)

    def find_key(self, key):
        for i, k in enumerate(self.keys):
            if k >= key:
                return i
        return len(self.keys)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def search(self, key):
        return self.root.search(key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.insert(0, root)
            new_root.split_child(0)
            self.root = new_root
        self.root.insert_non_full(key)

    def delete(self, key):
        if not self.root:
            return
        self.root.delete(key)
        if len(self.root.keys) == 0:
            if self.root.leaf:
                self.root = BTreeNode(self.t, True)
            else:
                self.root = self.root.children[0]

    def print_tree(self, node=None, indent=0):
        if node is None:
            node = self.root
        print(" " * indent + str(node.keys))
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, indent + 4)

btree = BTree(3)  # B-Tree of minimum degree 3

for key in [10, 20, 5, 6, 12, 30, 7, 17]:
    btree.insert(key)

print("Tree after insertion:")
btree.print_tree()

btree.delete(6)
btree.delete(13)  # Not present
btree.delete(7)

print("\nTree after deletion:")
btree.print_tree()

# Search
print("\nSearching for 17:", "Found" if btree.search(17) else "Not found")
print("Searching for 100:", "Found" if btree.search(100) else "Not found")