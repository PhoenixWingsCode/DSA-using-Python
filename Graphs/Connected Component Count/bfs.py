from collections import deque, defaultdict

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def count_connected_components(graph):
    visited = set()
    component_count = 0
    
    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)
            component_count += 1
            
    return component_count

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
    4: [5],
    5: [4]
}

print("Number of connected components:", count_connected_components(graph))
