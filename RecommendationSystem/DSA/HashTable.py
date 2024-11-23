class HashTableNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # For chaining


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        """Generate a hash for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        new_node = HashTableNode(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            # Collision handling using chaining
            current = self.table[index]
            while current:
                if current.key == key:
                    # Update value if key exists
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key):
        """Search for a value by its key."""
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        """Display the contents of the hash table."""
        for i, node in enumerate(self.table):
            print(f"Index {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")
