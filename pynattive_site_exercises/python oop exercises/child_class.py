# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

volvo_bus = Bus('Volvo', 140, 30)
print(volvo_bus.name)
print(volvo_bus.max_speed)
print(volvo_bus.mileage)