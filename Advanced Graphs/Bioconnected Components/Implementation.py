from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def biconnected_components(self):
        disc = [-1] * self.V  # Discovery times of visited vertices
        low = [-1] * self.V   # Lowest discovery time reachable
        parent = [-1] * self.V
        stack = []
        bcc = []

        def dfs(u):
            nonlocal bcc
            disc[u] = low[u] = self.time
            self.time += 1
            children = 0

            for v in self.graph[u]:
                if disc[v] == -1:  # If v is not visited
                    parent[v] = u
                    stack.append((u, v))
                    children += 1

                    dfs(v)

                    # Update low value of u for parent function calls
                    low[u] = min(low[u], low[v])

                    # If u is an articulation point, pop all edges in the stack
                    if (parent[u] == -1 and children > 1) or (parent[u] != -1 and low[v] >= disc[u]):
                        component = []
                        while stack[-1] != (u, v):
                            component.append(stack.pop())
                        component.append(stack.pop())
                        bcc.append(component)

                elif v != parent[u] and disc[v] < disc[u]:
                    # Update low value of u for back edge
                    low[u] = min(low[u], disc[v])
                    stack.append((u, v))

        for i in range(self.V):
            if disc[i] == -1:
                dfs(i)

                # If stack is not empty, pop all edges
                if stack:
                    component = []
                    while stack:
                        component.append(stack.pop())
                    bcc.append(component)

        return bcc


# Example Usage
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(5, 6)

biconnected_components = g.biconnected_components()
print("Biconnected Components:")
for component in biconnected_components:
    print(component)
