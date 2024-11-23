from DSA.DirectedGraph import DirectedGraph

class RecommendationService:
    def __init__(self, catalog_service, user_pref_service):
        self.user_product_graph = DirectedGraph()
        self.catalog_service = catalog_service  # Dependency Injection
        self.user_pref_service = user_pref_service  # Dependency Injection

    def add_interaction(self, user_id, product_id):
        """Add an interaction (e.g., view, purchase) between a user and a product."""
        self.user_product_graph.add_edge(user_id, product_id)

   
    
    def recommend_products(self, user_id):
        """Generate recommendations based on user interactions and preferences."""
        # Recommendations from interactions
        interaction_recommendations = []
        if user_id in self.user_product_graph.graph:
            interaction_recommendations = self.user_product_graph.graph[user_id]
        print(f"Interaction-based Recommendations for User {user_id}: {interaction_recommendations}")

        # Recommendations from preferences
        user_preferences = self.user_pref_service.get_preference(user_id)
        print(f"User Preferences for {user_id}: {user_preferences}")

        preference_recommendations = []
        if user_preferences:
            print(f"Matching preferences '{user_preferences}' with products.")
            user_keywords = {self.normalize(word) for word in user_preferences.split()}
            for product_id in range(101, 200):  # Simulated product IDs
                product = self.catalog_service.get_product(product_id)
                if product:
                    product_name = product.get("name", "").lower()
                    product_keywords = {self.normalize(word) for word in product_name.split()}
                    if user_keywords & product_keywords:  # Check for common normalized keywords
                        preference_recommendations.append(product_id)
                    print(f"Product {product_id}: {product_name}, Match: {user_keywords & product_keywords}")

        print(f"Preference-based Recommendations for User {user_id}: {preference_recommendations}")

        # Merge recommendations
        all_recommendations = list(set(interaction_recommendations + preference_recommendations))
        return all_recommendations
    
    def normalize(self,word):
        """Normalize a word by converting it to lowercase and handling plurals."""
        word = word.lower()
        if word.endswith('s'):  # Basic handling for plural forms
            word = word[:-1]
        return word

    def display_interactions(self):
        """Display all user-product interactions."""
        print("Current Interactions in the Graph:")
        self.user_product_graph.display()
    def display_interactions(self):
        """Display all user-product interactions."""
        print("Current Interactions in the Graph:")
        self.user_product_graph.display()
