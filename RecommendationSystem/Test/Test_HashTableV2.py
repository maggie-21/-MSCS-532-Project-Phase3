from DSA.HashTable import HashTable

def test_hash_table():
    ht = HashTable(size=5)
    ht.insert(101, {"name": "Laptop A", "price": 999})
    ht.insert(102, {"name": "Smartphone B", "price": 699})
    ht.insert(103, {"name": "Tablet C", "price": 499})
    ht.insert(104, {"name": "Smartwatch D", "price": 199})
    ht.insert(105, {"name": "Laptop B", "price": 1299})
    ht.insert(106, {"name": "Monitor E", "price": 299})  # Triggers resizing

    print("\n=== Hash Table Contents ===")
    ht.display()

    print("\n=== Search Test ===")
    assert ht.search(101)["name"] == "Laptop A"
    assert ht.search(105)["price"] == 1299
    assert ht.search(999) is None  # Non-existent key

    print("\n=== Deletion Test ===")
    ht.delete(103)
    assert ht.search(103) is None

    print("\n=== Final Hash Table ===")
    ht.display()

if __name__ == "__main__":
    test_hash_table()
