from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_bridges_util(self, u, visited, parent, low, disc, bridges):
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.find_bridges_util(v, visited, parent, low, disc, bridges)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_bridges(self):
        visited = [False] * self.V
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        bridges = []

        for i in range(self.V):
            if not visited[i]:
                self.find_bridges_util(i, visited, parent, low, disc, bridges)

        return bridges


# Example Usage
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)

    print("Bridges in the graph:")
    for u, v in g.find_bridges():
        print(f"{u} -- {v}")
