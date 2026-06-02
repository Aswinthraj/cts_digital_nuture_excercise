class Product:

    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name

    def display(self):
        return f"{self.product_id} - {self.name}"


class Perishable(Product):

    def __init__(self, product_id, name, expiry_date):
        super().__init__(product_id, name)
        self.expiry_date = expiry_date


class Electronics(Product):

    def __init__(self, product_id, name, warranty):
        super().__init__(product_id, name)
        self.warranty = warranty


inventory = {}

inventory["P101"] = {
    "product": Perishable("P101", "Milk", "2026-06-15"),
    "stock": 5
}

inventory["E201"] = {
    "product": Electronics("E201", "Laptop", "2 Years"),
    "stock": 25
}

inventory["P102"] = {
    "product": Perishable("P102", "Bread", "2026-06-05"),
    "stock": 3
}

low_stock = set()

for item in inventory.values():

    if item["stock"] < 10:
        low_stock.add(item["product"].name)

print("Inventory Summary")

for item in inventory.values():

    print(
        f"Product: {item['product'].name}, "
        f"Stock: {item['stock']}"
    )

print("\nLow Stock Alerts")

for product in low_stock:
    print(product)