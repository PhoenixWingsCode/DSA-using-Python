def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    
    if start == goal:
        return True
    
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    
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
goal_node = 'F'

if dfs(graph, start_node, goal_node):
    print(f"There is a path between {start_node} and {goal_node}.")
else:
    print(f"There is no path between {start_node} and {goal_node}.")
