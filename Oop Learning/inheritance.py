# Lets talk about inheritance, extend and override

'''
Notes:
Inheritance means take all the attributes from parent class to child class
'''


class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"name = {self.name}, age = {self.age}, salary = {self.salary}"
    
    def work(self):
        print(f"{self.name} is working...")

class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level
    
    def __str__(self):
        return super().__str__() + f", level = {self.level}"
    
    def debug(self):
        print(f'{self.name} is debugging...')

    def work(self): # overriding methods with same name of method.
        print(f"{self.name} is coding...")

class Designer(Employee):
    
    def draw(self):
        print(f"{self.name} is drawing...")

    def work(self): # overriding methods
        print(f"{self.name} is designing...")


se = SoftwareEngineer("ashwin", 28, 16800, "Junior")
# print(se)
# se.work()
# se.debug()


d = Designer("Vraj", 21, 10000)
# print(d)
# d.work()
# d.draw()


# Polymorphism (many forms)

employees = [SoftwareEngineer("ashwin", 28, 16800, "Junior"), SoftwareEngineer("akash", 30, 33000, "Senior"),Designer("Vraj", 21, 10000)]

for employee in employees:
    employee.work()

