class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        """Insert a new key-value pair into the BST."""
        print(f"Inserting key {key} with value {value} into BST.")
        if self.root is None:
            print(f"Creating root node for key {key} with value {value}.")
        self.root = self._insert(self.root, key, value)
        print(f"BST After Insert: {self.in_order_traversal()}")

    def _insert(self, node, key, value):
        if node is None:
            print(f"Creating new node for key {key} with value {value}.")
            return Node(key, value)
        if key < node.key:
            print(f"Traversing left: Current Node Key {node.key}")
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            print(f"Traversing right: Current Node Key {node.key}")
            node.right = self._insert(node.right, key, value)
        else:
            print(f"Updating node for key {key} with new value {value}.")
            node.value = value  # Update the value if the key already exists
        return node

    def search(self, key):
        """Search for a value by its key."""
        return self._search(self.root, key)
    def _search(self, node, key):
        if node is None:
            print(f"Search miss: Node is None for key {key}")
            return None
        if node.key == key:
            print(f"Search hit: Found key {key} with value {node.value}")
            return node
        if key < node.key:
            print(f"Traversing left: Searching for key {key} in left subtree.")
            return self._search(node.left, key)
        else:
            print(f"Traversing right: Searching for key {key} in right subtree.")
            return self._search(node.right, key)

  
    def in_order_traversal(self):
        """Return keys in sorted order."""
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append((node.key, node.value))
            self._in_order_traversal(node.right, result)
