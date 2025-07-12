from collections import deque

def zero_one_bfs(graph, start):
    # Number of nodes in the graph
    n = len(graph)
    
    # Distance array initialized to infinity
    dist = [float('inf')] * n
    dist[start] = 0
    
    # Deque for 0-1 BFS
    dq = deque([start])
    
    while dq:
        node = dq.popleft()
        
        for neighbor, weight in graph[node]:
            # Relaxation step
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                # Add to deque based on weight
                if weight == 0:
                    dq.appendleft(neighbor)
                else:
                    dq.append(neighbor)
    
    return dist

# Example usage:
# Graph represented as an adjacency list
# Each entry is a list of (neighbor, weight)
graph = {
    0: [(1, 0), (2, 1)],
    1: [(2, 0), (3, 1)],
    2: [(3, 0)],
    3: []
}

start_node = 0
distances = zero_one_bfs(graph, start_node)
print("Shortest distances from node", start_node, ":", distances)
