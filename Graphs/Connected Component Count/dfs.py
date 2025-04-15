def count_connected_components(graph):
    def dfs(node, visited):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    visited = set()
    component_count = 0

    for node in graph:
        if node not in visited:
            visited.add(node)
            dfs(node, visited)
            component_count += 1

    return component_count

# Example usage:
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3]
}

print(count_connected_components(graph))  # Output: 2
