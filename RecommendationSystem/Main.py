import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def post_request(endpoint, data):
    """Helper function to make POST requests."""
    response = requests.post(f"{BASE_URL}{endpoint}", json=data)
    print(f"POST {endpoint} | Data: {data} | Response: {response.json()}")
    return response.json()

def get_request(endpoint):
    """Helper function to make GET requests."""
    response = requests.get(f"{BASE_URL}{endpoint}")
    print(f"GET {endpoint} | Response: {response.json()}")
    return response.json()

def main():
    # 1. Add Users
    print("\n=== Adding Users ===")
    post_request("/add_user", {"user_id": 1, "name": "Alice"})
    post_request("/add_user", {"user_id": 2, "name": "Bob"})

    # 2. Add User Preferences
    print("\n=== Adding User Preferences ===")
    post_request("/add_user_preference", {"user_id": 1, "preference": "Laptops"})
    post_request("/add_user_preference", {"user_id": 2, "preference": "Smartphones"})

    # 3. Add Products
    print("\n=== Adding Products ===")
    post_request("/add_product", {"product_id": 101, "name": "Laptop A", "price": 999})
    post_request("/add_product", {"product_id": 102, "name": "Smartphone B", "price": 699})
    post_request("/add_product", {"product_id": 103, "name": "Laptop B", "price": 1299})
    post_request("/add_product", {"product_id": 104, "name": "Smartphone C", "price": 799})

    # 4. Add User-Product Interactions
    print("\n=== Adding User-Product Interactions ===")
    post_request("/add_interaction", {"user_id": 1, "product_id": 101})
    post_request("/add_interaction", {"user_id": 1, "product_id": 102})
    post_request("/add_interaction", {"user_id": 2, "product_id": 103})
    post_request("/add_interaction", {"user_id": 2, "product_id": 104})

    # 5. Get Recommendations
    print("\n=== Getting Recommendations ===")
    recommendations_user1 = get_request("/get_recommendations/1")
    recommendations_user2 = get_request("/get_recommendations/2")

    # Display Results
    print("\n=== Recommendations ===")
    print(f"User 1 Recommendations: {json.dumps(recommendations_user1, indent=2)}")
    print(f"User 2 Recommendations: {json.dumps(recommendations_user2, indent=2)}")

if __name__ == "__main__":
    main()
