import heapq

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (cost, current_vertex, previous_vertex)

    while min_heap:
        cost, current, prev = heapq.heappop(min_heap)
        if current in visited:
            continue
        visited.add(current)
        if prev is not None:
            mst.append((prev, current, cost))

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor, current))

    return mst

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

mst = prim(graph, 'A')
print("Minimum Spanning Tree:", mst)