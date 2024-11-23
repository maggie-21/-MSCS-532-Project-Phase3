from DSA.AVLTree import AVLTree

def test_avl_tree():
    avl = AVLTree()
    avl.insert(1, "Laptops")
    avl.insert(2, "Smartphones")
    avl.insert(3, "Tablets")
    print("In-order Traversal:", avl.in_order_traversal())
    assert avl.search(1).value == "Laptops"
    assert avl.search(2).value == "Smartphones"
    assert avl.search(3).value == "Tablets"

if __name__ == "__main__":
    test_avl_tree()
