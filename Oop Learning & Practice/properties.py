# property decorator using getter, setter and deleter

class SoftwareEngineer:
    def __init__(self, salary):
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        self.__salary = value
    
    @salary.deleter
    def salary(self):
        del self.__salary

se = SoftwareEngineer(6000)
se.salary = 7000
print(se.salary, 'salary--')

del se.salary
print(se.salary, 'salary--')