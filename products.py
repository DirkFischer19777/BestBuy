# products.py

class Product:
    """
    A class representing a product in the store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available stock quantity.
        active (bool): Whether the product is active (available for sale).
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new product instance.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Initial stock quantity.

        Raises:
            ValueError: If name is empty, price is negative, or quantity is negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product.
        If quantity reaches 0, the product becomes inactive.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints a string representation of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.

        Args:
            quantity (int): The amount to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If product is inactive, not enough stock, or invalid quantity.
        """
        if not self.active:
            raise ValueError("Product is inactive and cannot be purchased.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


# Test the class in the same file
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
