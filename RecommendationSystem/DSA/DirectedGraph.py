class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        """Add a new node to the graph."""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        """Add a directed edge from one node to another."""
        if from_node not in self.graph:
            self.add_node(from_node)
        if to_node not in self.graph:
            self.add_node(to_node)
        self.graph[from_node].append(to_node)

    def remove_node(self, node):
        """Remove a node and all its associated edges."""
        if node in self.graph:
            self.graph.pop(node)
        for edges in self.graph.values():
            if node in edges:
                edges.remove(node)

    def remove_edge(self, from_node, to_node):
        """Remove a directed edge from one node to another."""
        if from_node in self.graph and to_node in self.graph[from_node]:
            self.graph[from_node].remove(to_node)

    def bfs(self, start_node):
        """Perform Breadth-First Search (BFS) traversal."""
        visited = set()
        queue = [start_node]
        traversal = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                queue.extend(self.graph[node])

        return traversal

    def dfs(self, start_node, visited=None, traversal=None):
        """Perform Depth-First Search (DFS) traversal."""
        if visited is None:
            visited = set()
        if traversal is None:
            traversal = []

        visited.add(start_node)
        traversal.append(start_node)

        for neighbor in self.graph[start_node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, traversal)

        return traversal

    def display(self):
        """Display the graph as adjacency lists."""
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")
