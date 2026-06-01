def add_expenses(expenses,amount):
    if amount<=0:
        print("Invalid Expense Amount")
        return
    expenses.append(amount)
    print(f"Updated Expenses List : {expenses}")
expenses=[100, 250, 75]
add_expenses(expenses,150)