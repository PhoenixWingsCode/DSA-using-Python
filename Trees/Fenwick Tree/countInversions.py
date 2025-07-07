class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        sum_ = 0
        while index > 0:
            sum_ += self.tree[index]
            index -= index & -index
        return sum_

def count_inversions(arr):
    # Coordinate compression to handle large values
    rank_map = {val: idx + 1 for idx, val in enumerate(sorted(set(arr)))}
    ranked_arr = [rank_map[val] for val in arr]

    # Initialize Fenwick Tree
    max_val = len(rank_map)
    fenwick = FenwickTree(max_val)

    inversions = 0
    for i in range(len(ranked_arr) - 1, -1, -1):
        # Count elements smaller than the current element
        inversions += fenwick.query(ranked_arr[i] - 1)
        # Update Fenwick Tree with the current element
        fenwick.update(ranked_arr[i], 1)

    return inversions

# Example usage
arr = [8, 4, 2, 1]
print("Number of inversions:", count_inversions(arr))
