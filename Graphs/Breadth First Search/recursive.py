from collections import deque

# Define the graph using an adjacency list
graph = {
1: [2, 3, 4],
2: [5, 6],
3: [],
4: [7, 8],
5: [9, 10],
6: [],
7: [11, 12],
8: [],
9: [],
10: [],
11: [],
12: []
}

# Recursive BFS function
def recursive_bfs(graph, queue, discovered):
    if not queue:
        return

    # Dequeue the front node and print it
    v = queue.popleft()
    print(v, end=" ")

    # Enqueue all undiscovered adjacent nodes
    for u in graph[v]:
        if not discovered[u]:
            discovered[u] = True
            queue.append(u)

    # Recursive call
    recursive_bfs(graph, queue, discovered)

# Initialize the discovered list and queue
discovered = {key: False for key in graph}
queue = deque()

# Start BFS from the first node (1)
start_node = 1
discovered[start_node] = True
queue.append(start_node)

# Call the recursive BFS function
recursive_bfs(graph, queue, discovered)