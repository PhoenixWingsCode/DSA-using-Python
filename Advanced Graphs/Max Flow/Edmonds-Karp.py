from collections import deque

def bfs(capacity, flow, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque()
    queue.append(source)
    visited[source] = True
    while queue:
        u = queue.popleft()
        for v, cap in enumerate(capacity[u]):
            if not visited[v] and cap - flow[u][v] > 0:  # residual capacity > 0
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]
    parent = [-1] * n
    max_flow = 0

    while bfs(capacity, flow, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s!= source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        max_flow += path_flow

        v = sink
        while v!= source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow  # reverse flow
            v = parent[v]

    return max_flow

# Example graph represented by capacity matrix
capacity_matrix = [
    [0, 10, 10, 0],
    [0, 0, 5, 10],
    [0, 0, 0, 15],
    [0, 0, 0, 0]]


source_node = 0
sink_node = 3
print("Maximum flow:", edmonds_karp(capacity_matrix, source_node, sink_node))