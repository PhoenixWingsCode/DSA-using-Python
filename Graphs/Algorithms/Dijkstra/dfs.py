class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight

    def dfs_shortest_path(self, start, goal):
        stack = [(start, [start], 0)]
        shortest_path = None
        min_cost = float('inf')

        while stack:
            (node, path, cost) = stack.pop()
            if cost > min_cost:
                continue
            for neighbor in self.edges.get(node, []):
                if neighbor in path:
                    continue
                new_cost = cost + self.weights[(node, neighbor)]
                new_path = path + [neighbor]
                if neighbor == goal:
                    if new_cost < min_cost:
                        min_cost = new_cost
                        shortest_path = new_path
                else:
                    stack.append((neighbor, new_path, new_cost))

        return shortest_path, min_cost

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

shortest_path, cost = graph.dfs_shortest_path('A', 'D')
print(f"Shortest path: {shortest_path} with cost: {cost}")
