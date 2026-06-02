class Employee:
    def __init__(self,name):
        self.salary=0
        self.name=name
    def set_salary(self,salary):
        if salary <=0:
            print("Invalid Salary")
            return self
        self.salary=salary
        return self
    def appraisal(self,raiseamount):
        if raiseamount<=0:
            print("Invalid appraisal")
            return self
        self.salary+=raiseamount
        return self
    def display_salary(self):
        print(f"Employee: {self.name}")
        print(f"Final Salary : {self.salary}")
        
        return self
emp=Employee("Femilin")
emp.set_salary(50000).appraisal(5000).display_salary()
