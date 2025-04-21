def is_safe(v, pos, path, graph):
    # Check if this vertex is an adjacent vertex of the previously added vertex.
    if graph[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been included.
    if v in path:
        return False

    return True

def hamiltonian_cycle_util(graph, path, pos):
    # Base case: If all vertices are included in the path
    if pos == len(graph):
        # And if there is an edge from the last included vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Try different vertices as the next candidate in Hamiltonian Cycle.
    for v in range(1, len(graph)):
        if is_safe(v, pos, path, graph):
            path[pos] = v

            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True

            # Remove current vertex if it doesn't lead to a solution
            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Start from the first vertex

    if not hamiltonian_cycle_util(graph, path, 1):
        print("No Hamiltonian Cycle found")
        return False

    print("Hamiltonian Cycle found:")
    print(path + [path[0]])  # To show the cycle
    return True

# Example usage:
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonian_cycle(graph)