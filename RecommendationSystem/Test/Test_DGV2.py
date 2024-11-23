from DSA.DirectedGraph import DirectedGraph

def test_directed_graph():
    dg = DirectedGraph()

    # Add nodes and edges
    dg.add_edge("User1", "ProductA", {"interaction": "view", "weight": 1})
    dg.add_edge("User1", "ProductB", {"interaction": "purchase", "weight": 5})
    dg.add_edge("ProductA", "ProductB")
    dg.add_edge("User2", "ProductC")

    # Display the graph
    print("\n=== Graph ===")
    dg.display()

    # BFS and DFS
    print("\n=== BFS from User1 ===")
    print(dg.bfs("User1"))

    print("\n=== DFS from User1 ===")
    print(dg.dfs("User1"))

    # Remove edges and nodes
    print("\n=== Removing Edge User1 -> ProductB ===")
    dg.remove_edge("User1", "ProductB")
    dg.display()

    print("\n=== Removing Node ProductA ===")
    dg.remove_node("ProductA")
    dg.display()

if __name__ == "__main__":
    test_directed_graph()
