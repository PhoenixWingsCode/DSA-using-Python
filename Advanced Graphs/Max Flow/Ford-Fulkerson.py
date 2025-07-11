from collections import deque

# Function to perform BFS and find an augmenting path
def bfs(residual_graph, source, sink, parent):
    visited = [False] * len(residual_graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, capacity in enumerate(residual_graph[u]):
            if not visited[v] and capacity > 0:  # Check for unvisited and positive capacity
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:  # If sink is reached, return True
                    return True
    return False

# Ford-Fulkerson algorithm
def ford_fulkerson(graph, source, sink):
    residual_graph = [row[:] for row in graph]  # Create a copy of the graph as residual graph
    parent = [-1] * len(graph)
    max_flow = 0

    # Augment the flow while there is a path from source to sink
    while bfs(residual_graph, source, sink, parent):
        # Find the maximum flow through the path found by BFS
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Update residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency matrix
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    source = 0  # Source node
    sink = 5    # Sink node

    print("The maximum possible flow is:", ford_fulkerson(graph, source, sink))
