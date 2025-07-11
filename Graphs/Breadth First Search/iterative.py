from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
0: [1, 2],
1: [3, 4],
2: [4],
3: [],
4: []
}

print("BFS starting from vertex 0:")
bfs(graph, 0)