from collections import deque

def floyd_warshall(graph, num_vertices):
    # Initialize distance matrix with infinity
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Distance to self is 0
    for i in range(num_vertices):
        dist[i][i] = 0

    # Fill in weights from the adjacency list
    for u in range(num_vertices):
        for v, w in graph[u]:
            dist[u][v] = w

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def bfs(adj_list, start):
    visited = [False] * len(adj_list)
    queue = deque([start])
    visited[start] = True
    bfs_order = []

    while queue:
        vertex = queue.popleft()
        bfs_order.append(vertex)

        for neighbor, _ in adj_list[vertex]:  # Unpack tuple (neighbor, weight)
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return bfs_order

def floyd_warshall_bfs(graph):
    num_vertices = len(graph)
    dist = floyd_warshall(graph, num_vertices)

    bfs_orders = []
    for start in range(num_vertices):
        bfs_orders.append(bfs(graph, start))

    return dist, bfs_orders

# Example usage
graph = [
    [(1, 3), (2, 8), (4, -4)],
    [(3, 1), (4, 7)],
    [(1, 4)],
    [(0, 2), (2, -5)],
    [(3, 6)]
]

distances, bfs_orders = floyd_warshall_bfs(graph)

print("Shortest path distances:")
for row in distances:
    print(row)

print("\nBFS orders from each vertex:")
for i, order in enumerate(bfs_orders):
    print(f"From vertex {i}: {order}")
