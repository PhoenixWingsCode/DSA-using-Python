from collections import defaultdict

def dfs(graph, v, visited, stack=None):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    if stack is not None:
        stack.append(v)

def transpose_graph(graph, V):
    transposed = defaultdict(list)
    for v in range(V):
        for neighbor in graph[v]:
            transposed[neighbor].append(v)
    return transposed

def kosaraju_scc(graph, V):
    visited = [False] * V
    stack = []

    # Step 1: DFS on original graph to fill stack by finishing times
    for v in range(V):
        if not visited[v]:
            dfs(graph, v, visited, stack)

    # Step 2: Transpose graph
    transposed = transpose_graph(graph, V)

    # Step 3: DFS on transposed graph in order of stack
    visited = [False] * V
    sccs = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs(transposed, v, visited, component)
            sccs.append(component)

    return sccs

# Example usage:
if __name__ == "__main__":
    V = 5
    graph = defaultdict(list)
    graph[0].extend([2, 3])
    graph[1].append(0)
    graph[2].append(1)
    graph[3].append(4)

    sccs = kosaraju_scc(graph, V)
    print("Strongly Connected Components:")
    for i, comp in enumerate(sccs):
        print(f"Component {i+1}: {comp}")