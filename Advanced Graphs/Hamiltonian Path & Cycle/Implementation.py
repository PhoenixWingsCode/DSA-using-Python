class Hamiltonian:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.path = []

    def is_safe(self, v, pos):
        # Check if vertex v can be added to the path
        if self.graph[self.path[pos - 1]][v] == 0:
            return False
        if v in self.path:
            return False
        return True

    def hamiltonian_util(self, pos):
        # Base case: If all vertices are included in the path
        if pos == self.n:
            # Check if there's an edge back to the starting vertex for a cycle
            if self.graph[self.path[pos - 1]][self.path[0]] == 1:
                self.path.append(self.path[0])  # Form a cycle
                return True
            return False

        # Try different vertices as the next candidate
        for v in range(1, self.n):
            if self.is_safe(v, pos):
                self.path.append(v)
                if self.hamiltonian_util(pos + 1):
                    return True
                self.path.pop()  # Backtrack
        return False

    def find_hamiltonian_cycle(self):
        self.path = [0]  # Start from vertex 0
        if not self.hamiltonian_util(1):
            return None  # No Hamiltonian Cycle found
        return self.path

    def find_hamiltonian_path(self):
        for start in range(self.n):
            self.path = [start]
            if self.hamiltonian_util(1):
                return self.path
        return None  # No Hamiltonian Path found


# Example Usage
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

hamiltonian = Hamiltonian(graph)

# Find Hamiltonian Cycle
cycle = hamiltonian.find_hamiltonian_cycle()
print("Hamiltonian Cycle:", cycle if cycle else "None")

# Find Hamiltonian Path
path = hamiltonian.find_hamiltonian_path()
print("Hamiltonian Path:", path if path else "None")
