'''
Encapsulation:
bundling data into one(like zip folders) and hiding data like abstraction.

private attributes and public attributes
1. public attr = you can access attributes from ouside class
2. private attr = you can access only inside the class for outside it doesnt exists
'''

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name # public attributes
        self.age = age # public attributes
        self._salary = None # protectes attributes (you can access from outside world but for convention dont use it.) 
        self.__nums_bugs_solved = 0 # private attributes (can't access from outside)

    def code(self):
        self.__nums_bugs_solved += 1
    
    """To change particular private attribute we have need use a getter and setter"""
    # Getter
    def get_nums_bugs_solved(self):
        return self.__nums_bugs_solved

    # Setter
    def set_nums_bugs_solved(self, value):
        self.__nums_bugs_solved = value
    
    '''Lets calculate salary'''
    # Getter
    def get_salary(self):
        return self._salary
    
    # setter
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value): # protected method
        if self.__nums_bugs_solved < 10:
            return base_value * 1
        if self.__nums_bugs_solved < 100:
            return base_value * 2
        return base_value * 3
    
    

    
se = SoftwareEngineer('Hitesh', 26)

# se.set_nums_bugs_solved(12)


for _ in range(65):
    se.code()

se.set_salary(25000)

print(se.name, se.age, se._salary, se.get_nums_bugs_solved())





