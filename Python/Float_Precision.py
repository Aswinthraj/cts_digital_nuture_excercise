def calculate_net_salary(salary, tax_rate):
    if salary < 0:
        print("Invalid Salary")
        return

    if tax_rate < 0 or tax_rate > 1:
        print("Invalid tax Rate")
        return

    tax_amount = salary * tax_rate
    net_salary = salary - tax_amount

    print(f"Salary : {salary:.2f}")
    print(f"Tax Rate : {tax_rate:.2f}")
    print(f"Net Salary : {net_salary:.2f}")

salary = 75000.5
tax_rate = 0.18

calculate_net_salary(salary, tax_rate)