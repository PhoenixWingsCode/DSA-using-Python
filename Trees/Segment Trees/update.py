class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = (arr[start], arr[start])  # (min, max)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = (
                min(self.tree[left_child][0], self.tree[right_child][0]),
                max(self.tree[left_child][1], self.tree[right_child][1])
            )

    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = (value, value)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(idx, value, left_child, start, mid)
            else:
                self.update(idx, value, right_child, mid + 1, end)
            self.tree[node] = (
                min(self.tree[left_child][0], self.tree[right_child][0]),
                max(self.tree[left_child][1], self.tree[right_child][1])
            )

    def query(self, l, r, node, start, end):
        if r < start or l > end:
            return (float('inf'), float('-inf'))  # (min, max)
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_query = self.query(l, r, left_child, start, mid)
        right_query = self.query(l, r, right_child, mid + 1, end)
        return (
            min(left_query[0], right_query[0]),
            max(left_query[1], right_query[1])
        )

    def range_query(self, l, r):
        return self.query(l, r, 0, 0, self.n - 1)

    def point_update(self, idx, value):
        self.update(idx, value, 0, 0, self.n - 1)


# Example usage:
arr = [1, 3, 2, 7, 9, 11]
seg_tree = SegmentTree(arr)

# Query range [1, 4] for min and max
print("Range Query [1, 4]:", seg_tree.range_query(1, 4))  # Output: (2, 9)

# Update index 3 to value 5
seg_tree.point_update(3, 5)

# Query range [1, 4] again after update
print("Range Query [1, 4] after update:", seg_tree.range_query(1, 4))  # Output: (2, 9)
