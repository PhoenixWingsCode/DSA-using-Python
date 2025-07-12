from collections import deque

def is_bipartite(graph):
    """
    Check if a graph is bipartite and return the coloring if it is.
    
    :param graph: Dictionary representing an adjacency list of the graph.
    :return: Tuple (True, coloring) if bipartite, else (False, None).
    """
    color = {}
    for node in graph:
        if node not in color:
            # Start BFS from this node
            queue = deque([node])
            color[node] = 0  # Assign the first color (0)
            
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        # Assign the opposite color to the neighbor
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        # If a neighbor has the same color, it's not bipartite
                        return False, None
    return True, color


# Example Usage
if __name__ == "__main__":
    # Example graph as an adjacency list
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    
    is_bipartite_graph, coloring = is_bipartite(graph)
    if is_bipartite_graph:
        print("The graph is bipartite.")
        print("Coloring:", coloring)
    else:
        print("The graph is not bipartite.")
