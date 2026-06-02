class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def print_detail(self):
        print(f"Employee Name is : {self.name}")
        print(f"Salary is : {self.salary}")
emp1=Employee("Hari",60000)
emp2=Employee("Femilin",60000)
emp1.print_detail()
emp2.print_detail()