from Service.UserPreferenceService import UserPreferenceService
from Service.CatalogService import CatalogService
from Service.RecommendationService import RecommendationService

# Initialize services
user_pref_service = UserPreferenceService()
catalog_service = CatalogService()
recommendation_service = RecommendationService()

# Test UserPreferenceService
user_pref_service.add_preference(1, "Laptops")
user_pref_service.add_preference(2, "Smartphones")
print("User 1's Preference:", user_pref_service.get_preference(1))
print("All Preferences:", user_pref_service.get_all_preferences())

# Test CatalogService
catalog_service.add_product(101, {"name": "Laptop A", "price": 999})
catalog_service.add_product(102, {"name": "Smartphone B", "price": 699})
print("Product 101 Details:", catalog_service.get_product(101))
catalog_service.display_catalog()

# Test RecommendationService
recommendation_service.add_interaction("User1", "ProductA")
recommendation_service.add_interaction("User1", "ProductB")
print("Recommendations for User1:", recommendation_service.recommend_products("User1"))
recommendation_service.display_interactions()
