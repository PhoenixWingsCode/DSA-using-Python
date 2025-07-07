class DisjointSet:
    def __init__(self, size):
        # Initialize parent and rank arrays
        self.parent = [i for i in range(size)]  # Each element is its own parent initially
        self.rank = [0] * size  # Rank is used for union by rank optimization

    def find(self, x):
        # Path compression optimization
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Recursively find the root
        return self.parent[x]

    def union(self, x, y):
        # Union by rank optimization
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        # Check if two elements are in the same set
        return self.find(x) == self.find(y)

# Create a disjoint set with 5 elements (0 to 4)
ds = DisjointSet(5)

# Perform unions
ds.union(0, 1)
ds.union(1, 2)

# Check connectivity
print(ds.connected(0, 2))  # Output: True
print(ds.connected(0, 3))  # Output: False

# Find representative of a set
print(ds.find(2))  # Output: 0 (or the root of the set containing 2)