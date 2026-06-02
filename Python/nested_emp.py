def get_salary(data,department,employee):
    if department not in data:
        print("Department not found")
        return
    if employee not in data[department]:
        print("Department not found")
        return
    print(f"Salary  : {data[department][employee]}")
employess={
    "IT":{
        "Allen":50000,
        "Raj":60000
    },
    "HR":{
        "Suba":50000,
        "Joy":55000
    }
}
get_salary(employess,"IT","Raj")