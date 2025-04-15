from collections import deque

def bfs_path_exists(graph, start, end):
    if start == end:
        return True
    
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == end:
                    return True
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return False

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'F'
print(bfs_path_exists(graph, start_node, end_node))  # Output: True
