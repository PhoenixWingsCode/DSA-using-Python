class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False  # Already connected
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True


# Merge Sort for Edges
def merge_sort(edges):
    if len(edges) <= 1:
        return edges
    mid = len(edges) // 2
    left = merge_sort(edges[:mid])
    right = merge_sort(edges[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_edges = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:  # Compare by weight
            sorted_edges.append(left[i])
            i += 1
        else:
            sorted_edges.append(right[j])
            j += 1
    sorted_edges.extend(left[i:])
    sorted_edges.extend(right[j:])
    return sorted_edges


def kruskal(n, edges):
    sorted_edges = merge_sort(edges)
    dsu = DisjointSet(n)
    mst_weight = 0
    mst_edges = []

    for u, v, w in sorted_edges:
        if dsu.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges


# Example usage:
nodes = 5
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

weight, mst = kruskal(nodes, edges)
print("Total Weight of MST:", weight)
print("Edges in MST:", mst)