# class HashTableNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None  # For chaining


# class HashTable:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [None] * self.size

#     def _hash(self, key):
#         """Generate a hash for a given key."""
#         return hash(key) % self.size

#     def insert(self, key, value):
#         """Insert a key-value pair into the hash table."""
#         index = self._hash(key)
#         new_node = HashTableNode(key, value)

#         if self.table[index] is None:
#             self.table[index] = new_node
#         else:
#             # Collision handling using chaining
#             current = self.table[index]
#             while current:
#                 if current.key == key:
#                     # Update value if key exists
#                     current.value = value
#                     return
#                 if current.next is None:
#                     break
#                 current = current.next
#             current.next = new_node

#     def search(self, key):
#         """Search for a value by its key."""
#         index = self._hash(key)
#         current = self.table[index]
#         while current:
#             if current.key == key:
#                 return current.value
#             current = current.next
#         return None

#     def delete(self, key):
#         """Delete a key-value pair from the hash table."""
#         index = self._hash(key)
#         current = self.table[index]
#         prev = None

#         while current:
#             if current.key == key:
#                 if prev is None:
#                     self.table[index] = current.next
#                 else:
#                     prev.next = current.next
#                 return True
#             prev = current
#             current = current.next
#         return False

#     def display(self):
#         """Display the contents of the hash table."""
#         for i, node in enumerate(self.table):
#             print(f"Index {i}:", end=" ")
#             current = node
#             while current:
#                 print(f"({current.key}: {current.value})", end=" -> ")
#                 current = current.next
#             print("None")
class HashNode:
    """Node to store key-value pairs in the hash table."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # For chaining

class HashTable:
    """Optimized Hash Table with dynamic resizing."""
    def __init__(self, size=20):
        self.size = size
        self.table = [None] * self.size
        self.num_elements = 0
        self.load_factor_threshold = 0.75  # Resize when load factor exceeds this

    def _hash(self, key):
        """Compute the hash index for a key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        print(f"Inserting key {key} at index {index}.")
        node = self.table[index]

        # Update the value if key already exists
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next

        # Insert new node
        new_node = HashNode(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.num_elements += 1

        # Check and resize if load factor exceeds threshold
        if self.load_factor() > self.load_factor_threshold:
            self._resize()

    def search(self, key):
        """Search for a value by key."""
        index = self._hash(key)
        print(f"Searching for key {key} at index {index}.")
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        """Delete a key-value pair."""
        index = self._hash(key)
        print(f"Deleting key {key} from index {index}.")
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.num_elements -= 1
                return node.value
            prev = node
            node = node.next
        return None

    def load_factor(self):
        """Calculate the current load factor of the hash table."""
        return self.num_elements / self.size

    def _resize(self):
        """Resize the hash table to reduce collisions."""
        print("Resizing hash table...")
        old_table = self.table
        self.size *= 2  # Double the size
        self.table = [None] * self.size
        self.num_elements = 0

        # Rehash all elements into the new table
        for node in old_table:
            while node:
                self.insert(node.key, node.value)
                node = node.next

    def display(self):
        """Display the contents of the hash table."""
        for i, node in enumerate(self.table):
            print(f"Index {i}:", end=" ")
            while node:
                print(f"({node.key}: {node.value})", end=" -> ")
                node = node.next
            print("None")
