class User:
    def __init__(self, user_id, name, preferences=None):
        self.user_id = user_id
        self.name = name
        self.preferences = preferences or []  # List of user preferences

    def __repr__(self):
        return f"User(user_id={self.user_id}, name='{self.name}', preferences={self.preferences})"
