from collections import deque, defaultdict

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)
    component_size = 0
    
    while queue:
        node = queue.popleft()
        component_size += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return component_size

def largest_component(graph):
    visited = set()
    max_size = 0
    
    for node in graph:
        if node not in visited:
            component_size = bfs(graph, node, visited)
            max_size = max(max_size, component_size)
    
    return max_size

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
    4: [5],
    5: [4]
}

print("The size of the largest component is:", largest_component(graph))
