from DSA.DirectedGraph import DirectedGraph

# Initialize the Directed Graph
graph = DirectedGraph()

# Add nodes
graph.add_node("User1")
graph.add_node("ProductA")
graph.add_node("ProductB")

# Add edges
graph.add_edge("User1", "ProductA")
graph.add_edge("User1", "ProductB")
graph.add_edge("ProductA", "ProductB")

# Display the graph
print("Graph structure:")
graph.display()

# Test BFS
print("BFS from User1:", graph.bfs("User1"))

# Test DFS
print("DFS from User1:", graph.dfs("User1"))

# Remove an edge and display the graph
graph.remove_edge("User1", "ProductA")
print("Graph after removing edge User1 -> ProductA:")
graph.display()

# Remove a node and display the graph
graph.remove_node("ProductB")
print("Graph after removing node ProductB:")
graph.display()
