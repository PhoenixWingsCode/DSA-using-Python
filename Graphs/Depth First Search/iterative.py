def iterative_dfs(graph, start):
    visited = set() # Set to keep track of visited nodes
    stack = [start] # Initialize the stack with the start node

    while stack:
        vertex = stack.pop() # Pop a vertex from the stack
        if vertex not in visited:
            print(vertex, end=" ") # Print the visited node
        visited.add(vertex) # Mark the node as visited
        # Add all unvisited adjacent nodes to the stack
        stack.extend(graph[vertex] - visited)

# Example usage
graph = {
'0': {'1', '2'},
'1': {'0', '3', '4'},
'2': {'0'},
'3': {'1'},
'4': {'2', '3'}
}

iterative_dfs(graph, '0')