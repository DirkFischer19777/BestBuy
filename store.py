
# store.py

from typing import List, Tuple
from products import Product


class Store:
    """
    A class representing a store that contains multiple products.
    Provides methods for managing inventory and processing orders.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes the store with a list of products.

        Args:
            products (List[Product]): Initial list of products in the store.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a new product to the store.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove.

        Raises:
            ValueError: If the product is not found in the store.
        """
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in store.")

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: Sum of all product quantities.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Returns all active products in the store.

        Returns:
            List[Product]: List of active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order consisting of multiple products.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of (Product, quantity) tuples.

        Returns:
            float: The total price of the order.

        Raises:
            ValueError: If any product is invalid or quantity cannot be fulfilled.
        """
        total_price = 0.0

        # First pass: validate all purchases
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.name} is not available in this store.")
            if not product.is_active():
                raise ValueError(f"{product.name} is inactive and cannot be purchased.")
            if quantity > product.get_quantity():
                raise ValueError(f"Not enough stock for {product.name}.")

        # Second pass: perform purchases
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


# Test code
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    products = best_buy.get_all_products()
    print("Total quantity in store:", best_buy.get_total_quantity())
    print("Order total:", best_buy.order([(products[0], 1), (products[1], 2)]))
