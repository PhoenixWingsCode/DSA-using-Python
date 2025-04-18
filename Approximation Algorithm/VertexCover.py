def vertex_cover(graph):
    # Initialize an empty set to store the vertex cover
    cover = set()
    
    # Create a copy of the edges to work with
    edges = set(graph['edges'])
    
    while edges:
        # Pick an arbitrary edge (u, v)
        u, v = edges.pop()
        
        # Add both vertices of the edge to the cover
        cover.add(u)
        cover.add(v)
        
        # Remove all edges incident to either u or v
        edges = {e for e in edges if u not in e and v not in e}
    
    return cover

# Example usage
graph = {
    'vertices': {1, 2, 3, 4, 5},
    'edges': {(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)}
}

cover = vertex_cover(graph)
print("Vertex Cover:", cover)