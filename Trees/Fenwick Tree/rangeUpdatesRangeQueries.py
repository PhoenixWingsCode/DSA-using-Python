class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & (-idx)

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s

class FenwickRangeUpdateRangeQuery:
    def __init__(self, n):
        self.n = n
        self.BIT1 = FenwickTree(n)
        self.BIT2 = FenwickTree(n)

    def range_update(self, l, r, val):
        # 1-indexed indexes
        self.BIT1.update(l, val)
        self.BIT1.update(r + 1, -val)
        self.BIT2.update(l, val * (l - 1))
        self.BIT2.update(r + 1, -val * r)

    def prefix_sum(self, idx):
        return self.BIT1.query(idx) * idx - self.BIT2.query(idx)

    def range_query(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

# Example usage:
frurq = FenwickRangeUpdateRangeQuery(10)
frurq.range_update(2, 5, 3)  # add 3 to range [2, 5]
print(frurq.range_query(1, 5)) # should print 12 (3*4 elements from 2 to 5)
print(frurq.range_query(3, 3)) # should print 3