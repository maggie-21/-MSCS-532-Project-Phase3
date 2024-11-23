from Controller.UserController import UserController
from Controller.ProductController import ProductController
from Controller.RecommendationController import RecommendationController

# Initialize controllers
user_controller = UserController()
product_controller = ProductController()
recommendation_controller = RecommendationController()

# Add users
print("\n=== Adding Users ===")
user_controller.add_user(1, "Alice")
user_controller.add_user(2, "Bob")

# Add preferences
print("\n=== Adding User Preferences ===")
user_controller.add_user_preference(1, "Laptops")
user_controller.add_user_preference(2, "Smartphones")

# Add products
print("\n=== Adding Products ===")
product_controller.add_product(101, "Laptop A", 999)
product_controller.add_product(102, "Smartphone B", 699)

# Add interactions
print("\n=== Adding User-Product Interactions ===")
recommendation_controller.add_interaction(1, 101)
recommendation_controller.add_interaction(1, 102)

# Generate recommendations
print("\n=== Generating Recommendations ===")
recommendation_controller.get_recommendations(1)
