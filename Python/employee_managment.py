import json


class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"


def save_employees(employees):

    data = {}

    for emp_id, emp in employees.items():
        data[emp_id] = {
            "name": emp.name,
            "salary": emp.salary
        }

    with open("emps.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Employee data saved successfully")


def load_employees():

    try:
        with open("emps.json", "r") as file:
            data = json.load(file)

        employees = {}

        for emp_id, details in data.items():
            employees[emp_id] = Employee(
                emp_id,
                details["name"],
                details["salary"]
            )

        return employees

    except FileNotFoundError:
        print("File not found")
        return {}


employees = {
    "E101": Employee("E101", "John", 50000),
    "E102": Employee("E102", "Alice", 60000),
    "E103": Employee("E103", "Bob", 45000)
}

save_employees(employees)

loaded_employees = load_employees()

print("\nEmployee Details")

for emp in loaded_employees.values():
    print(emp)