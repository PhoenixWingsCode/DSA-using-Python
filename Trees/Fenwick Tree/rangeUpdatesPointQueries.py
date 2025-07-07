class FenwickTreeRangeUpdatePointQuery:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n+1)

    def update(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & (-idx)

    def range_update(self, l, r, delta):
        # Add delta to range [l, r]
        self.update(l, delta)
        self.update(r+1, -delta)

    def point_query(self, idx):
        # Query value at idx
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & (-idx)
        return result

# Example usage:
ft = FenwickTreeRangeUpdatePointQuery(10)
ft.range_update(2, 5, 10)   # Add 10 to elements 2 through 5
print(ft.point_query(3))    # Should return 10
print(ft.point_query(6))    # Should return 0