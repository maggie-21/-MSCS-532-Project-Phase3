from DSA.BinarySearchTree import BinarySearchTree

class UserPreferenceService:
    def __init__(self):
        self.preference_tree = BinarySearchTree()
        print("Initialized UserPreferenceService with an empty BST.")

    # def add_preference(self, user_id, preference):
    #     """Add or update a user's preference."""
    #     print(f"Adding preference: User {user_id} -> {preference}")

    #     self.preference_tree.insert(user_id, preference)
    #     print(f"BST After Insertion: {self.preference_tree.in_order_traversal()}")

    def add_preference(self, user_id, preference):
        """Add or update a user's preference."""
        user_id = int(user_id)  # Ensure user_id is an integer
        print(f"Adding preference: User {user_id} -> {preference}")
        self.preference_tree.insert(user_id, preference)
        print(f"BST After Insertion: {self.preference_tree.in_order_traversal()}")

    def get_preference(self, user_id):
        """Retrieve a user's preference by ID."""
        user_id = int(user_id)  # Ensure user_id is an integer
        node = self.preference_tree.search(user_id)
        print(f"Retrieved preference for User {user_id}: {node.value if node else None}")
        return node.value if node else None


    def get_all_preferences(self):
        """Retrieve all preferences in sorted order."""
        return self.preference_tree.in_order_traversal()
