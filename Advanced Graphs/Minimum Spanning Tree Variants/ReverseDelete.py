class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: set() for i in range(vertices)}
        self.edges = []

    def add_edge(self, u, v, w):
        self.graph[u].add((v, w))
        self.graph[v].add((u, w))
        self.edges.append((w, u, v))

    def is_connected(self):
        visited = [False] * self.V

        def dfs(u):
            visited[u] = True
            for (nbr, _) in self.graph[u]:
                if not visited[nbr]:
                    dfs(nbr)

        # Start DFS from vertex 0
        dfs(0)
        return all(visited)

    def reverse_delete_mst(self):
        # Sort edges by decreasing weight
        self.edges.sort(reverse=True)
        mst_weight = 0

        for w, u, v in self.edges[:]:
            # Remove edge
            self.graph[u].remove((v, w))
            self.graph[v].remove((u, w))

            if not self.is_connected():
                # Re-add edge if removal disconnects graph
                self.graph[u].add((v, w))
                self.graph[v].add((u, w))
                mst_weight += w  # Keep edge in MST

        print("Edges in MST:")
        for u in self.graph:
            for v, w in self.graph[u]:
                # To avoid printing twice for undirected edges
                if u < v:
                    print(f"Edge {u} - {v} with weight {w}")
        print(f"Total weight of MST: {mst_weight}")

# Example Usage

g = Graph(7)
edges = [(0,1,7), (0,3,5), (1,2,8), (1,4,7), (1,3,9), (3,4,15),
         (3,5,6), (2,4,5), (4,5,8), (4,6,9), (5,6,11)]
for u, v, w in edges:
    g.add_edge(u, v, w)

g.reverse_delete_mst()