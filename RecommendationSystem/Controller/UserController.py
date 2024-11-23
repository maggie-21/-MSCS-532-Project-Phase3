class UserController:
    def __init__(self, user_service):
        self.user_service = user_service  # Shared UserPreferenceService instance
        self.users = {}  # In-memory storage for user details

    def add_user(self, user_id, name):
        """Add a new user."""
        if user_id in self.users:
            return {"message": f"User {user_id} already exists."}, 400
        self.users[user_id] = {"user_id": user_id, "name": name}
        return {"message": f"User {name} added successfully."}, 201

    def add_user_preference(self, user_id, preference):
        """Add or update a user's preference."""
        if user_id not in self.users:
            return {"message": f"User {user_id} not found."}, 404
        self.user_service.add_preference(user_id, preference)
        return {"message": f"Preference '{preference}' added for User {user_id}."}, 200

    def get_user_preferences(self, user_id):
        """Retrieve a user's preferences."""
        if user_id not in self.users:
            return {"message": f"User {user_id} not found."}, 404
        preferences = self.user_service.get_preference(user_id)
        return {"user_id": user_id, "preferences": preferences}, 200
