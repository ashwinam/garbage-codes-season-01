# Exercise 7: Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)


# display_student("Emma", 26)

show_student = display_student


show_student('Emma', 28)
