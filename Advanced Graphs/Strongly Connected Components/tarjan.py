def tarjan(graph):
    n = len(graph)
    index = [-1] * n           # Discovery times of nodes
    low_link = [-1] * n        # Lowest discovered node reachable
    on_stack = [False] * n     # To check if node is in stack
    stack = []
    result = []
    index_counter = 0

    def dfs(v):
        nonlocal index_counter
        index[v] = index_counter
        low_link[v] = index_counter
        index_counter += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if index[w] == -1:  # If not visited
                dfs(w)
                low_link[v] = min(low_link[v], low_link[w])
            elif on_stack[w]:   # Update low_link if in stack (back edge)
                low_link[v] = min(low_link[v], index[w])

        # If v is head of SCC, pop the stack
        if low_link[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            result.append(scc)

    for v in range(n):
        if index[v] == -1:
            dfs(v)

    return result

# Example graph as adjacency list:
graph = [
    [1],        # 0 -> 1
    [2, 4, 5],  # 1 -> 2, 4, 5
    [3, 6],     # 2 -> 3, 6
    [2, 7],     # 3 -> 2, 7
    [0, 5],     # 4 -> 0, 5
    [6],        # 5 -> 6
    [5],        # 6 -> 5
    [3, 6]]      # 7 -> 3, 6


print(tarjan(graph))