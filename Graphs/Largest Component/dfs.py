def dfs(graph, node, visited):
    stack = [node]
    size = 0
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            size += 1
            stack.extend(graph[current] - visited)
    return size

def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        if node not in visited:
            component_size = dfs(graph, node, visited)
            largest = max(largest, component_size)
    return largest

# Example usage:
graph = {
    0: {1, 2},
    1: {0, 3},
    2: {0},
    3: {1},
    4: {5},
    5: {4}
}

print(largest_component(graph))  # Output: 4
