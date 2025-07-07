class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.representative = None  # Points to the representative of the set


class DisjointSet:
    def __init__(self):
        self.representatives = {}  # Maps representative to the head of the linked list

    def make_set(self, data):
        """Creates a new set with a single element."""
        node = Node(data)
        node.representative = node  # Initially, the node is its own representative
        self.representatives[node] = node
        return node

    def find(self, node):
        """Finds the representative of the set containing the node."""
        return node.representative

    def union(self, node1, node2):
        """Unites the sets containing node1 and node2."""
        rep1 = self.find(node1)
        rep2 = self.find(node2)

        if rep1 == rep2:
            return  # Already in the same set

        # Merge the two linked lists
        head1 = self.representatives[rep1]
        head2 = self.representatives[rep2]

        # Append list2 to the end of list1
        current = head1
        while current.next:
            current = current.next
        current.next = head2

        # Update the representative for all nodes in list2
        current = head2
        while current:
            current.representative = rep1
            current = current.next

        # Update the representatives dictionary
        self.representatives.pop(rep2)
        self.representatives[rep1] = head1


# Example Usage
ds = DisjointSet()

# Create sets
node1 = ds.make_set(1)
node2 = ds.make_set(2)
node3 = ds.make_set(3)
node4 = ds.make_set(4)

# Perform unions
ds.union(node1, node2)
ds.union(node3, node4)
ds.union(node1, node3)

# Find representatives
print(ds.find(node1).data)  # Output: 1
print(ds.find(node4).data)  # Output: 1