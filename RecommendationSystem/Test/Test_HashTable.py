from DSA.HashTable import HashTable

# Initialize Hash Table
hash_table = HashTable()

# Insert products
hash_table.insert(101, "Product A")
hash_table.insert(102, "Product B")
hash_table.insert(103, "Product C")
hash_table.insert(104, "Product D")

# Test search
print("Search for key 102:", hash_table.search(102))  # Should return "Product B"

# Test delete
hash_table.delete(103)
print("Search for key 103 (after deletion):", hash_table.search(103))  # Should return None

# Display table
hash_table.display()
