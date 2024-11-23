from DSA.HashTable import HashTable

class CatalogService:
    def __init__(self):
        self.product_catalog = HashTable(size=20)

    def add_product(self, product_id, product_details):
        """Add or update a product in the catalog."""
        self.product_catalog.insert(product_id, product_details)

    def get_product(self, product_id):
        """Retrieve product details by ID."""
        return self.product_catalog.search(product_id)

    def delete_product(self, product_id):
        """Delete a product from the catalog."""
        return self.product_catalog.delete(product_id)

    def display_catalog(self):
        """Display the entire product catalog."""
        self.product_catalog.display()
