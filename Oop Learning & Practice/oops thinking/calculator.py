'''
We want to make a console simple app with four main functions: addition, subtraction, division and multiplication.

First of all we need a core. But before core we will define our Function class. It must be simple.

'''

class Function:
    def __init__(self, name, function):
        self.__name = name
        self.__function = function

    @property
    def name(self):
        return self.__name
    
    @property
    def function(self):
        return self.__function
    

class Core:
    def __init__(self, *args):
        self.__function = args
        self.__exc_function = dict()
        self.__build_dict()

    def __build_dict(self):
        for function in self.__function:
            self.__exc_function[function.name] = function.function
    
    def get_function(self, key):
        return self.__exc_function.get(key)
    

class CoreBuilder:
    def __init__(self):
        self.__addition = Function(name="add", function=lambda a, b: a+b)
        self.__subtraction = Function(name="sub", function=lambda a, b: a-b)
        self.__division = Function(name="div", function=lambda a, b: a/b)
        self.__multiplication = Function(name="mul", function=lambda a, b: a*b)
        self._core = Core(self.__addition,
                          self.__subtraction,
                          self.__division,
                          self.__multiplication)
        
    @property
    def core(self):
        return self._core
    

builder = CoreBuilder()
name = 'add'
a = 10
b = 5

function = builder.core.get_function(name)
print(function(a,b))


class Executor:
    def __init__(self, core):
        self.core_builder = core

    def execute(self, name, a, b):
        function = self.core_builder.core.get_function(name)
        if function is not None:
            return function(a, b)
        else:
            return "No matching command"
        
class Reader:
    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__command = ""
    
    def read_data(self, string):
        self.__a, self.__command, self.__b = string.split(" ")
        self.__a = int(self.__a)
        self.__b = int(self.__b)
    
    def get_data(self):
        return self.__a, self.__command, self.__b


class Calculator:
    def __init__(self):
        self._builder = CoreBuilder()
        self._executor = Executor(self._builder)
        self._reader = Reader()
        self.command = None
        self.a = 0
        self.b = 0

    def perform_operation(self, string):
        self._reader.read_data(string)
        self.a, self.command, self.b = self._reader.get_data()
        print(self._executor.execute(self.command, self.a, self.b))


class Runner:
    def __init__(self, run=False):
        self.calculator = Calculator()
        if run:
            while True:
                print("Enter your command like this")
                string = input()
                if string == "exit":
                    break
                else:
                    self.calculator.perform_operation(string)


runner = Runner(run=True)
