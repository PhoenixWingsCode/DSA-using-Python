import sys
from collections import defaultdict
import heapq

# Helper function: Bellman-Ford algorithm
def bellman_ford(graph, V, src):
    dist = [float('inf')] * V
    dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles
    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # Negative weight cycle detected

    return dist

# Helper function: Dijkstra's algorithm
def dijkstra(adj_list, src, V):
    dist = [float('inf')] * V
    dist[src] = 0
    pq = [(0, src)]  # Priority queue (min-heap)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist

# Johnson's algorithm
def johnsons_algorithm(graph, V):
    # Step 1: Add a new vertex and connect it to all other vertices with weight 0
    new_graph = graph + [(V, v, 0) for v in range(V)]
    h = bellman_ford(new_graph, V + 1, V)

    if h is None:
        return "Graph contains a negative weight cycle"

    # Step 2: Reweight the edges
    reweighted_graph = []
    for u, v, w in graph:
        reweighted_graph.append((u, v, w + h[u] - h[v]))

    # Step 3: Run Dijkstra's algorithm for each vertex
    adj_list = defaultdict(list)
    for u, v, w in reweighted_graph:
        adj_list[u].append((v, w))

    all_pairs_shortest_paths = []
    for u in range(V):
        dist = dijkstra(adj_list, u, V)
        # Adjust distances back to original weights
        adjusted_dist = [d + h[v] - h[u] if d != float('inf') else float('inf') for v, d in enumerate(dist)]
        all_pairs_shortest_paths.append(adjusted_dist)

    return all_pairs_shortest_paths

# Example usage
if __name__ == "__main__":
    # Graph represented as (u, v, w) where u -> v with weight w
    graph = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    V = 5  # Number of vertices

    result = johnsons_algorithm(graph, V)
    print("All-Pairs Shortest Paths:")
    for row in result:
        print(row)
