from collections import defaultdict, deque

class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.rev_graph = defaultdict(list)
        self.assignment = [False] * n

    def add_clause(self, u, v):
        # Add implications for the clause (u OR v)
        self.graph[-u].append(v)
        self.graph[-v].append(u)
        self.rev_graph[v].append(-u)
        self.rev_graph[u].append(-v)

    def _dfs(self, graph, node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self._dfs(graph, neighbor, visited, stack)
        stack.append(node)

    def _reverse_post_order(self):
        visited = set()
        stack = []
        for i in range(-self.n, self.n + 1):
            if i != 0 and i not in visited:
                self._dfs(self.graph, i, visited, stack)
        return stack

    def _assign_scc(self, stack):
        visited = set()
        scc = {}
        while stack:
            node = stack.pop()
            if node not in visited:
                component = []
                self._dfs_collect(self.rev_graph, node, visited, component)
                for v in component:
                    scc[v] = component
        return scc

    def _dfs_collect(self, graph, node, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self._dfs_collect(graph, neighbor, visited, component)

    def solve(self):
        stack = self._reverse_post_order()
        scc = self._assign_scc(stack[::-1])

        for i in range(1, self.n + 1):
            if i in scc and -i in scc and scc[i] == scc[-i]:
                return False  # Unsatisfiable

        # Assign truth values
        order = sorted(scc.keys(), key=lambda x: len(scc[x]), reverse=True)
        assigned = {}
        for var in order:
            if var not in assigned:
                assigned[var] = True
                assigned[-var] = False

        for i in range(1, self.n + 1):
            self.assignment[i - 1] = assigned[i]

        return True

# Example usage
n = 3  # Number of variables
solver = TwoSAT(n)

# Add clauses (x1 OR x2), (¬x1 OR x3), (¬x2 OR ¬x3)
solver.add_clause(1, 2)
solver.add_clause(-1, 3)
solver.add_clause(-2, -3)

if solver.solve():
    print("Satisfiable")
    print("Assignment:", solver.assignment)
else:
    print("Unsatisfiable")
