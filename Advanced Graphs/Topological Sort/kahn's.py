from collections import defaultdict, deque

def topological_sort_kahn(vertices, edges):
    # Step 1: Initialize in-degree and adjacency list
    in_degree = {i: 0 for i in range(vertices)}
    adjacency_list = defaultdict(list)

    # Step 2: Build the graph
    for u, v in edges:
        adjacency_list[u].append(v)
        in_degree[v] += 1

    # Step 3: Collect nodes with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []

    # Step 4: Process nodes in the queue
    while queue:
        current = queue.popleft()
        topo_order.append(current)

        # Decrease in-degree of neighbors
        for neighbor in adjacency_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 5: Check for cycles
    if len(topo_order) != vertices:
        raise ValueError("The graph is not a DAG (contains a cycle).")

    return topo_order

# Example usage
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

try:
    result = topological_sort_kahn(vertices, edges)
    print("Topological Order:", result)
except ValueError as e:
    print(e)
