class Interaction:
    def __init__(self, user_id, product_id, interaction_type):
        self.user_id = user_id
        self.product_id = product_id
        self.interaction_type = interaction_type  # e.g., 'view', 'purchase'

    def __repr__(self):
        return f"Interaction(user_id={self.user_id}, product_id={self.product_id}, interaction_type='{self.interaction_type}')"
