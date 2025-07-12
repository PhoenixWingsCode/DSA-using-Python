from collections import defaultdict, deque
import math

def dials_algorithm(graph, source, max_weight):
    """
    Dial's Algorithm for shortest paths in a graph with non-negative integer weights.
    
    :param graph: Dictionary representing the adjacency list of the graph.
                  Format: {node: [(neighbor, weight), ...]}
    :param source: The starting node.
    :param max_weight: Maximum edge weight in the graph.
    :return: Dictionary of shortest distances from the source to each node.
    """
    # Initialize distances and buckets
    distances = {node: math.inf for node in graph}
    distances[source] = 0
    num_buckets = max_weight + 1
    buckets = [deque() for _ in range(num_buckets)]
    buckets[0].append(source)
    
    # Process buckets
    current_distance = 0
    while any(buckets):
        # Find the next non-empty bucket
        while not buckets[current_distance % num_buckets]:
            current_distance += 1
        
        # Process nodes in the current bucket
        node = buckets[current_distance % num_buckets].popleft()
        for neighbor, weight in graph[node]:
            new_distance = distances[node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                bucket_index = new_distance % num_buckets
                buckets[bucket_index].append(neighbor)
    
    return distances

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    source = 0
    max_weight = 5  # Maximum edge weight in the graph
    shortest_distances = dials_algorithm(graph, source, max_weight)
    print("Shortest distances from source:", shortest_distances)
