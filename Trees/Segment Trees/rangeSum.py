class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Allocate memory for the segment tree
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]  # Leaf node
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]  # Combine results

    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = value  # Update leaf node
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(idx, value, left_child, start, mid)
            else:
                self.update(idx, value, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]  # Recalculate

    def query(self, l, r, node, start, end):
        if r < start or l > end:  # No overlap
            return 0
        if l <= start and end <= r:  # Total overlap
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.query(l, r, left_child, start, mid)
        right_sum = self.query(l, r, right_child, mid + 1, end)
        return left_sum + right_sum

# Example Usage
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

# Query range sum from index 1 to 3
print(seg_tree.query(1, 3, 0, 0, len(arr) - 1))  # Output: 15

# Update index 2 to value 10
seg_tree.update(2, 10, 0, 0, len(arr) - 1)

# Query again after update
print(seg_tree.query(1, 3, 0, 0, len(arr) - 1))  # Output: 20
