# OOP Exercise 5: Define a property that must have the same value for every class instance (object)

'''
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white
'''

class Vehicle:
    __color = 'White'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    # lets do with property
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus('Volvo Bus', 150, 15)
bus.color = 'Blue'
print(bus.color)

car = Car('Maruti Suzuki 800', 100, 40)
print(car.color)