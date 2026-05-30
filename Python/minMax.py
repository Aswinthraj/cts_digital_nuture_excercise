def mimMax(salaries):
    if len(salaries)==0:
        print("Invalid List")
        return
    highest_salary=max(salaries)
    lowest_salary=min(salaries)
    print(f"Highest Salary : {highest_salary}")
    print(f"Lowest Salary:{lowest_salary}")
salaries=[50000, 75000, 62000, 95000]
mimMax(salaries)