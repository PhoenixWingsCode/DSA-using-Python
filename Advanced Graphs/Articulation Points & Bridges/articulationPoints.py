from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def _articulation_point_util(self, u, visited, parent, low, disc, ap):
        children = 0
        visited[u] = True
        disc[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                self._articulation_point_util(v, visited, parent, low, disc, ap)

                low[u] = min(low[u], low[v])

                if parent[u] is None and children > 1:
                    ap[u] = True
                if parent[u] is not None and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_articulation_points(self):
        visited = [False] * self.V
        disc = [float('inf')] * self.V
        low = [float('inf')] * self.V
        parent = [None] * self.V
        ap = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self._articulation_point_util(i, visited, parent, low, disc, ap)

        return [index for index, value in enumerate(ap) if value]

# Example Usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

articulation_points = g.find_articulation_points()
print("Articulation Points:", articulation_points)
