# Creating class


class SoftwareEngineer: # it's a blueprint
    
    alias = "Keyboard Mechs" # class attributes(accessed by both class and instance)

    def __init__(self, name, age, designation, salary): # instance attributes(only accessed by instances)
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
    
    def code(self): # instance related function
        print(f"{self.name} is writting code...")
    
    # with parameter
    def code_in_language(self, language):
        print(f"{self.name} is writting code in {language}")

    # with returning value
    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.designation}"
        return information

#instanciating variable(object)
se1 = SoftwareEngineer("rahul", 25, "Backend Developer", "25k")
se2 = SoftwareEngineer("shrimati", 22, "Frontend Developer", "35k")
# print(se1.name, se1.age)
# print(se1.alias) # class attribute access by instance
# print(SoftwareEngineer.alias) # accessed by class

# print(se2.name, se2.age)

# Functions in classes or methods

se1.code()

se2.code()

se1.code_in_language('Python')

se2.code_in_language('Javascript')

print(se1.information())
print(se2.information())

