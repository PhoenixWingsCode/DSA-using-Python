class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

# Example usage:
n = 10  # Size of the array
fenwick = FenwickTree(n)

# Update values
fenwick.update(3, 5)  # Add 5 to index 3
fenwick.update(5, 2)  # Add 2 to index 5

# Query prefix sum
print(fenwick.prefix_sum(5))  # Sum of elements from index 1 to 5

# Query range sum
print(fenwick.range_sum(3, 5))  # Sum of elements from index 3 to 5
