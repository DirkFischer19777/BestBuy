# main.py

import products
import store


def start(store_obj: store.Store):
    """
    Starts the interactive menu for the store.
    Provides options to list products, check total amount,
    make an order, or quit.
    """
    while True:
        print("\nWelcome to Best Buy Store! 🛒")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            print("\nAvailable Products:")
            for idx, product in enumerate(store_obj.get_all_products(), start=1):
                print(f"{idx}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")

        elif choice == "2":
            total = store_obj.get_total_quantity()
            print(f"\nTotal items in store: {total}")

        elif choice == "3":
            order_list = []
            products_available = store_obj.get_all_products()

            if not products_available:
                print("No active products available for order.")
                continue

            print("\nChoose products to order (enter 0 to finish):")
            for idx, product in enumerate(products_available, start=1):
                print(f"{idx}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")

            while True:
                try:
                    selection = int(input("\nEnter product number (0 to finish): "))
                    if selection == 0:
                        break
                    if selection < 1 or selection > len(products_available):
                        print("Invalid product number, try again.")
                        continue

                    product = products_available[selection - 1]
                    quantity = int(input(f"Enter quantity for {product.name}: "))

                    order_list.append((product, quantity))

                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            if order_list:
                try:
                    total_price = store_obj.order(order_list)
                    print(f"\nOrder successful! Total cost: {total_price} dollars.")
                except ValueError as e:
                    print(f"Order failed: {e}")

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    start(best_buy)
