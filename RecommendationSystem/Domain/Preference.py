class Preference:
    def __init__(self, user_id, preference_type):
        self.user_id = user_id
        self.preference_type = preference_type

    def __repr__(self):
        return f"Preference(user_id={self.user_id}, preference_type='{self.preference_type}')"
