class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is working")
class Manager(Employee):
    def work(self):
        print("Manager is Managing")
class Tester(Employee):
    def work(self):
        print("Tester is testing the application")
class Deployer(Employee):
    def work(self):
        print("Deployer is Working to Deploy")        
emlpoye=[Developer(),Manager(),Tester(),Deployer()]
for emp in emlpoye:
    emp.work()
