def update_employee(emp1,emp2):
    if not emp1 or not emp2:
        print("Invalid Details")
        return
    emp1.update(emp2)

    print("Updated Employee Details")
    print(emp1)
employee1={
    "name":"John",
    "salary":5000
}
employee2={
    "name":"Aries",
    "salary":6000
}
update_employee(employee1,employee2)
