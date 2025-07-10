from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Adjacency list
        self.V = vertices  # Number of vertices

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Recursive function for DFS and topological sorting
    def dfs(self, v, visited, stack):
        visited[v] = True  # Mark the current node as visited

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)

        # Push the current vertex to the stack (stores the result)
        stack.append(v)

    # Function to perform topological sort
    def topological_sort(self):
        visited = [False] * self.V  # Mark all vertices as not visited
        stack = []  # Stack to store the topological order

        # Call the recursive helper function for all vertices
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Return the reversed stack as the topological order
        return stack[::-1]


# Example usage
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Topological Sort of the graph:")
    print(g.topological_sort())
