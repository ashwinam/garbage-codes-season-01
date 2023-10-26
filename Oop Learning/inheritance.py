# Lets talk about inheritance, extend and override

'''
Notes:
Inheritance means take all the attributes from parent class to child class
'''


class Employee:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name = {self.name}, age = {self.age}."
    
    def work(self):
        print(f"{self.name} is working...") 

class SoftwareEngineer(Employee):
    pass

class Designer(Employee):
    pass


se = SoftwareEngineer("ashwin", 28)
print(se)
se.work()


d = Designer("Vraj", 21)
print(d)
d.work()