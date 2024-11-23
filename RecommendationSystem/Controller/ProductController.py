from Service.CatalogService import CatalogService
from Domain.Product import Product

class ProductController:
    def __init__(self, catalog_service):
        self.catalog_service = catalog_service  # Shared CatalogService instance
        self.products = {}  # In-memory storage for product details

    def add_product(self, product_id, name, price):
        """Add a new product to the catalog."""
        if product_id in self.products:
            return {"message": f"Product {product_id} already exists."}, 400
        product = Product(product_id, name, price)
        self.products[product_id] = product
        self.catalog_service.add_product(product_id, vars(product))
        return {"message": f"Product {name} added successfully."}, 201

    def get_product(self, product_id):
        """Retrieve a product by its ID."""
        product = self.catalog_service.get_product(product_id)
        if not product:
            return {"message": f"Product {product_id} not found."}, 404
        return {"product": product}, 200
