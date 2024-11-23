import random
import time
import requests

BASE_URL = "http://127.0.0.1:5000"


def generate_users_bulk(num_users, batch_size=440):
    """Generate and upload users in bulk."""
    session = requests.Session()
    for i in range(0, num_users, batch_size):
        users = []
        for user_id in range(i + 1, i + 1 + batch_size):
            users.append({"user_id": user_id, "name": f"User{user_id}"})
        response = session.post(f"{BASE_URL}/add_bulk_users", json={"users": users})
        print(f"Batch {i // batch_size + 1}: {response.status_code}")
def generate_preferences_bulk(num_users, batch_size=500):
    """Generate and upload user preferences in bulk."""
    session = requests.Session()
    preferences = ["Laptops", "Smartphones", "Tablets", "Headphones", "Watches"]
    for i in range(0, num_users, batch_size):
        preference_batch = []
        for user_id in range(i + 1, i + 1 + batch_size):
            preference_batch.append({
                "user_id": user_id,
                "preference": random.choice(preferences)
            })
        response = session.post(f"{BASE_URL}/add_bulk_preferences", json={"preferences": preference_batch})
        print(f"Batch {i // batch_size + 1}: {response.status_code}")

def generate_products_bulk(num_products, batch_size=100):
    """Generate and upload products in batches."""
    session = requests.Session()
    for i in range(0, num_products, batch_size):
        products = []
        for product_id in range(i + 101, i + 101 + batch_size):
            products.append({
                "product_id": product_id,
                "name": f"Product{product_id}",
                "price": random.randint(50, 1000)
            })
        response = session.post(f"{BASE_URL}/add_bulk_products", json={"products": products})
        print(f"Batch {i // batch_size + 1}: {response.status_code}")

def generate_interactions_bulk(num_users, num_interactions, batch_size=500):
    """Generate and upload interactions in batches."""
    session = requests.Session()
    for i in range(0, num_interactions, batch_size):
        interactions = []
        for _ in range(batch_size):
            user_id = random.randint(1, num_users)
            product_id = random.randint(101, 101 + 50000)  # Assuming 50,000 products
            interactions.append({"user_id": user_id, "product_id": product_id})
        response = session.post(f"{BASE_URL}/add_bulk_interactions", json={"interactions": interactions})
        print(f"Batch {i // batch_size + 1}: {response.status_code}")

def test_recommendations(num_tests, num_users):
    """Fetch recommendations for random users."""
    session = requests.Session()
    for _ in range(num_tests):
        user_id = random.randint(1, num_users)
        start_time = time.time()
        response = session.get(f"{BASE_URL}/get_recommendations/{user_id}")
        end_time = time.time()
        print(f"Recommendations for User {user_id}: {response.json()} | Time: {end_time - start_time:.2f}s")

if __name__ == "__main__":
    # Stress test parameters
    NUM_USERS = 10000
    NUM_PRODUCTS = 50000
    NUM_INTERACTIONS = 100000
    NUM_TESTS = 1000
    BATCH_SIZE = 500

    # print("\n=== Generating Users ===")
    # generate_users(NUM_USERS)

    print("\n=== Generating Users in Bulk ===")
    generate_users_bulk(NUM_USERS, BATCH_SIZE)
    
    print("\n=== Generating User Preferences in Bulk ===")
    generate_preferences_bulk(NUM_USERS, BATCH_SIZE)

    print("\n=== Generating Products in Bulk ===")
    generate_products_bulk(NUM_PRODUCTS, BATCH_SIZE)

    print("\n=== Generating Interactions in Bulk ===")
    generate_interactions_bulk(NUM_USERS, NUM_INTERACTIONS, BATCH_SIZE)

    print("\n=== Testing Recommendations ===")
    test_recommendations(NUM_TESTS, NUM_USERS)
