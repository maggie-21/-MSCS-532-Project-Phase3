from DSA.BinarySearchTree import BinarySearchTree

# Initialize BST
bst = BinarySearchTree()

# Insert some user preferences
bst.insert(1, "Preference A")
bst.insert(3, "Preference C")
bst.insert(2, "Preference B")
bst.insert(4, "Preference D")

# Search for a key
result = bst.search(3)
print(f"Found: {result.key}, {result.value}" if result else "Not Found")

# In-order traversal
print("In-order Traversal:", bst.in_order_traversal())
