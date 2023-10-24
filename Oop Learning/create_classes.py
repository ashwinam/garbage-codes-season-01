# Creating class


class SoftwareEngineer: # it's a blueprint
    
    alias = "Keyboard Mechs" # class attributes(accessed by both class and instance)

    def __init__(self, name, age, designation, salary): # instance attributes(only accessed by instances)
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary

#instanciating variable(object)
se1 = SoftwareEngineer("rahul", 25, "Backend Developer", "25k")
print(se1.name, se1.age)
print(se1.alias) # class attribute access by instance
print(SoftwareEngineer.alias) # accessed by class



