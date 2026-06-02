import math


class CartItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):

        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item_name} Removed")
                return

        print("Item Not Found")

    def calculate_total(self):

        total = 0

        for item in self.items:
            total += item.price * item.quantity

        return total

    def print_receipt(self):

        subtotal = self.calculate_total()
        gst = subtotal * 0.18
        final_total = subtotal + gst

        print("------ RECEIPT ------")

        for item in self.items:
            print(
                f"{item.name} | ₹{item.price} x {item.quantity}"
            )

        print(f"\nSubtotal : ₹{subtotal:.2f}")
        print(f"GST (18%) : ₹{gst:.2f}")
        print(f"Final Total : ₹{final_total:.2f}")


cart = ShoppingCart()

cart.add_item(CartItem("Laptop", 50000, 1))
cart.add_item(CartItem("Mouse", 500, 2))
cart.add_item(CartItem("Keyboard", 1000, 1))

cart.remove_item("Mouse")

cart.print_receipt()