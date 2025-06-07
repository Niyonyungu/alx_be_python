"""
Scope refers to the visibility of variables and functions in certain parts of your code.
There are two types of scope in Python:
1. Local Scope: Variables defined within a function are not accessible from outside the function.
2. Global Scope: Variables defined outside of any function are accessible from anywhere in the code.

"""

def person(name):
    message = f"Hello, {name}!"
    return message
    

print(person("John"))  

def area_triangle(base, height):
    area = f"The area is , 0.5 * {base} * {height}"
    return area
print(area_triangle(5, 10))

def is_number_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."    