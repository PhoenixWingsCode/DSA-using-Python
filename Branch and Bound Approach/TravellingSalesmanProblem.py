from itertools import permutations

def calculate_distance(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]  # Return to the starting point
    return distance

def travelling_salesman(graph):
    n = len(graph)
    vertices = list(range(n))
    min_path = None
    min_distance = float('inf')
    
    for perm in permutations(vertices):
        current_distance = calculate_distance(graph, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm
    
    return min_path, min_distance

# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, distance = travelling_salesman(graph)
print(f"Shortest path: {path}")
print(f"Minimum distance: {distance}")
