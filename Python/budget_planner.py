import matplotlib.pyplot as plt


class Category:

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount

        if self.spent > self.limit:
            print(f"Alert! {self.name} exceeded budget limit.")

    def display(self):
        print(
            f"{self.name}: "
            f"Spent = ₹{self.spent}, "
            f"Limit = ₹{self.limit}"
        )


categories = {
    "Food": Category("Food", 5000),
    "Transport": Category("Transport", 3000),
    "Entertainment": Category("Entertainment", 2000)
}

while True:

    category = input(
        "Enter Category (Food/Transport/Entertainment) or 'done': "
    )

    if category.lower() == "done":
        break

    if category not in categories:
        print("Invalid Category")
        continue

    amount = float(input("Enter Expense: "))

    categories[category].add_expense(amount)

print("\nBudget Summary")

for cat in categories.values():
    cat.display()

labels = []
sizes = []

for cat in categories.values():
    labels.append(cat.name)
    sizes.append(cat.spent)

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Monthly Budget Spending")
plt.show()