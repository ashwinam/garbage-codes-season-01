'''
Object priented programming is a programming paradigm that based on objects and object is a blueprint or template of a class, and class contains data and code(attributes and behavious),


To understand oop lets take a example of cat describe cat:

1. Lets define properties of a cat:
name: maserati,
legs: 4,
eyes: 2
nose: 1
ears: 2
have_tail: True,
color: brown,
mood: happy

2. Let's define behavious of a cat:
sleep,
eat,
hugs,
walk,
'''

# Now we know about cat, then lets create cat class

class Cat:
    """
    It is a cat. It's carnivore.
    """
    # Now we need to specify a constructor.
    # Constructor - is a first method to call after
    # class instance creation.
    def __init__(self, name, color):
        """
        :param name: str(), required to specify while creation
        :param color: str(), required to specify while creation
        """
        self.name = name
        self.color = color
        self.have_tail = True
        self.legs = 4
        self.nose = 1
        self.ears = 2
        self.eyes = 2

    # Next we need to add methods to the class
    # but we will use pass statement.
    # So it means now these methods are useless
    # but they will be needed later.

    def sleep(self):
        """
        Method to make cat sleep for t hours
        :param t: int(), count of seconds to sleep
        :return: void/nothing
        """
        pass

    def eat(self):
        pass

