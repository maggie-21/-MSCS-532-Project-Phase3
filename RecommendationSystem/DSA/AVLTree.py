class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1  # Height of the node
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, key, value):
        """Insert a new key-value pair into the AVL tree."""
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return AVLNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # Update the value if the key already exists
            node.value = value
            return node

        # Update the height of the node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Get the balance factor
        balance = self.get_balance(node)

        # Perform rotations if the node becomes unbalanced
        # Left Heavy
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        # Right Heavy
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        # Left-Right Heavy
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Right-Left Heavy
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def search(self, key):
        """Search for a key in the AVL tree."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def in_order_traversal(self):
        """Return the in-order traversal of the AVL tree."""
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append((node.key, node.value))
            self._in_order_traversal(node.right, result)
