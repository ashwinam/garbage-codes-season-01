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
    
    """To change particular private attribute we have need use a getter and setter"""
    # Getter
    def get_nums_bugs_solved(self):
        return self.__nums_bugs_solved

    # Setter
    def set_nums_bugs_solved(self, value):
        self.__nums_bugs_solved = value
    
    
se = SoftwareEngineer('Hitesh', 26)

se.set_nums_bugs_solved(12)

print(se.name, se.age, se._salary, se.get_nums_bugs_solved())



