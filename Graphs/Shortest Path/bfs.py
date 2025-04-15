from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Keep track of visited nodes
    visited = set()
    # Queue for BFS
    queue = deque([[start]])
    
    # If the start is the goal
    if start == goal:
        return [start]
    
    # Loop until there are nodes to explore
    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]
        
        # If node has not been visited
        if node not in visited:
            neighbors = graph[node]
            # Go through all neighbor nodes, construct a new path and push it into the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                # Return path if neighbor is the goal
                if neighbor == goal:
                    return new_path
            
            # Mark node as visited
            visited.add(node)
    
    # Return None if no path is found
    return None

# Example usage
graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

start = 'A'
goal = 'G'
print(bfs_shortest_path(graph, start, goal))
