def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    if start == end:
        return True
    
    if start in visited:
        return False
    
    visited.add(start)
    
    for neighbor in graph[start]:
        if has_path(graph, neighbor, end, visited):
            return True
    
    return False

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(has_path(graph, 'A', 'F'))  # Output: True
print(has_path(graph, 'A', 'D'))  # Output: True
print(has_path(graph, 'A', 'G'))  # Output: False
