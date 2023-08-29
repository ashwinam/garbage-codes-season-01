# Exercise 4: Create a function with a default argument


def show_employee(name, salary=9000):
    print(f'Name: {name}, Salary: {salary}')


show_employee("Ben", 12000)
show_employee("Jessica")
