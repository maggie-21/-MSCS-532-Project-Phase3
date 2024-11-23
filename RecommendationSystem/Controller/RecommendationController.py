from Service.RecommendationService import RecommendationService

class RecommendationController:
    def __init__(self, catalog_service, user_pref_service):
        self.recommendation_service = RecommendationService(catalog_service, user_pref_service)

    def add_interaction(self, user_id, product_id):
        """Add a user-product interaction."""
        self.recommendation_service.add_interaction(user_id, product_id)
        return {"message": f"Interaction added: User {user_id} -> Product {product_id}."}, 201

    def get_recommendations(self, user_id):
        """Generate recommendations for a user."""
        recommendations = self.recommendation_service.recommend_products(user_id)
        if not recommendations:
            return {"message": f"No recommendations found for User {user_id}."}, 404
        return {"user_id": user_id, "recommendations": recommendations}, 200
