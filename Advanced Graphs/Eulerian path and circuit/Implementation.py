from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def _dfs(self, v, visited):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    def is_connected(self):
        visited = set()
        # Find a vertex with a non-zero degree
        start_vertex = next((v for v in self.graph if self.graph[v]), None)
        if not start_vertex:
            return True  # No edges in the graph
        self._dfs(start_vertex, visited)
        # Check if all vertices with edges are visited
        return all(v in visited or not self.graph[v] for v in self.graph)

    def find_eulerian(self):
        if not self.is_connected():
            return "Graph is not connected, no Eulerian Path or Circuit."

        odd_degree_vertices = [v for v in self.graph if len(self.graph[v]) % 2 != 0]

        if len(odd_degree_vertices) == 0:
            return "Graph has an Eulerian Circuit."
        elif len(odd_degree_vertices) == 2:
            return "Graph has an Eulerian Path."
        else:
            return "Graph has neither an Eulerian Path nor Circuit."

# Example Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

print(g.find_eulerian())  # Output: Graph has an Eulerian Path.
