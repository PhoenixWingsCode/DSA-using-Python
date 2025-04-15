from collections import deque

def has_path_bfs(graph, start, goal):
    if start == goal:
        return True

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current == goal:
            return True

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

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

start_node = 'A'
goal_node = 'F'

print(has_path_bfs(graph, start_node, goal_node))  # Output: True
