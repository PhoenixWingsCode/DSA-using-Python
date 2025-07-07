class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [None] * (4 * self.n)
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
            left_min, left_max = self.tree[left_child]
            right_min, right_max = self.tree[right_child]
            self.tree[node] = (min(left_min, right_min), max(left_max, right_max))

    def query(self, node, start, end, l, r):
        if r < start or l > end:  # No overlap
            return (float('inf'), float('-inf'))  # Neutral values for min and max
        if l <= start and end <= r:  # Total overlap
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_min, left_max = self.query(left_child, start, mid, l, r)
        right_min, right_max = self.query(right_child, mid + 1, end, l, r)
        return (min(left_min, right_min), max(left_max, right_max))

    def range_query(self, l, r):
        return self.query(0, 0, self.n - 1, l, r)


# Example usage:
arr = [1, 3, 2, 7, 9, 11]
seg_tree = SegmentTree(arr)

# Query for range [1, 4]
min_val, max_val = seg_tree.range_query(1, 4)
print(f"Minimum: {min_val}, Maximum: {max_val}")
