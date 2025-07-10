class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent to self and rank to 0 for all elements
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Find the root of set x belongs to with path compression
        if self.parent[x]!= x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        # Union by rank of the sets containing x and y
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return  # Already in the same set
        
        # Attach smaller rank tree under larger rank tree root
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

dsu = DisjointSetUnion(5)
dsu.union(0, 1)
dsu.union(1, 2)
print(dsu.find(2))  # Output: 0 or representative of set containing 2
print(dsu.find(3))  # Output: 3, since 3 is in its own set initially