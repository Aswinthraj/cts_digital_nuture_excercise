import csv

def analyze_employees():

    try:

        employees = []

        with open("employees.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                row["salary"] = int(row["salary"])
                employees.append(row)

        high_salary = [
            emp for emp in employees
            if emp["salary"] > 50000
        ]

        average_salary = sum(
            emp["salary"] for emp in employees
        ) / len(employees)

        print("Employee Data")
        print(employees)

        print("\nEmployees with Salary > 50000")
        print(high_salary)

        print(f"\nAverage Salary: {average_salary:.2f}")

    except FileNotFoundError:
        print("File not found")

    except ValueError:
        print("Invalid salary data")


analyze_employees()