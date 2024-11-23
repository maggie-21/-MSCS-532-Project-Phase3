# from flask import Flask, request, jsonify
# from Controller.UserController import UserController
# from Controller.ProductController import ProductController
# from Controller.RecommendationController import RecommendationController
# from Service.CatalogService import CatalogService
# from Service.UserPreferenceService import UserPreferenceService

# # Initialize Flask app and services
# app = Flask(__name__)
# catalog_service = CatalogService()
# user_pref_service = UserPreferenceService()

# # Initialize controllers
# user_controller = UserController()
# product_controller = ProductController()
# recommendation_controller = RecommendationController(catalog_service, user_pref_service)
from flask import Flask, request, jsonify
from Controller.UserController import UserController
from Controller.ProductController import ProductController
from Controller.RecommendationController import RecommendationController
from Service.CatalogService import CatalogService
from Service.UserPreferenceService import UserPreferenceService

# Initialize Flask app
app = Flask(__name__)

# Shared service instances
catalog_service = CatalogService()
user_pref_service = UserPreferenceService()

# Initialize controllers with shared services
user_controller = UserController(user_pref_service)
product_controller = ProductController(catalog_service)
recommendation_controller = RecommendationController(catalog_service, user_pref_service)

@app.route('/')
def home():
    """Default route to check if the server is running."""
    return jsonify({
        "message": "Welcome to the Recommendation System API!",
        "endpoints": {
            "POST /add_user": "Add a new user",
            "POST /add_user_preference": "Add a user preference",
            "POST /add_product": "Add a new product",
            "GET /get_product/<product_id>": "Retrieve product details",
            "POST /add_interaction": "Add a user-product interaction",
            "GET /get_recommendations/<user_id>": "Get recommendations for a user"
        }
    }), 200

# === User Endpoints ===
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user_id = data.get('user_id')
    name = data.get('name')
    response, status_code = user_controller.add_user(user_id, name)
    return jsonify(response), status_code

@app.route('/add_user_preference', methods=['POST'])
def add_user_preference():
    data = request.json
    user_id = int(data.get('user_id'))  # Convert to integer
    preference = data.get('preference')
    response, status_code = user_controller.add_user_preference(user_id, preference)
    return jsonify(response), status_code

# === Product Endpoints ===
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    product_id = data.get('product_id')
    name = data.get('name')
    price = data.get('price')
    response, status_code = product_controller.add_product(product_id, name, price)
    return jsonify(response), status_code

@app.route('/get_product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    response, status_code = product_controller.get_product(product_id)
    return jsonify(response), status_code

# === Interaction and Recommendation Endpoints ===
@app.route('/add_interaction', methods=['POST'])
def add_interaction():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    response, status_code = recommendation_controller.add_interaction(user_id, product_id)
    return jsonify(response), status_code

# @app.route('/get_recommendations/<user_id>', methods=['GET'])
# def get_recommendations(user_id):
#     # Display interactions for debugging
#     recommendation_controller.recommendation_service.display_interactions()
#     response, status_code = recommendation_controller.get_recommendations(user_id)
#     recommendation_controller.recommendation_service.display_interactions()
#     return jsonify(response), status_code
@app.route('/get_recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    user_id = int(user_id)  # Convert to integer
    response, status_code = recommendation_controller.get_recommendations(user_id)
    return jsonify(response), status_code

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
