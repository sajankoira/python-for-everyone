"""
TOPIC: Functions - Don't Repeat Yourself (DRY)
WHAT: Block of reusable code
WHY: Write once, use many times. Makes code clean & testable.
"""

# --- Simple Function ---
def greet():
    print("Hello, Welcome to Python!")

greet()  # Call function
greet()

# --- Function with Parameters ---
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Arjun")
greet_person("Priya")

# --- Function with Return ---
def add(a, b):
    result = a + b
    return result

sum_val = add(5, 3)
print(f"5+3={sum_val}")

# If no return, returns None
def no_return():
    print("I do something but return nothing")

x = no_return()
print(f"x is {x}")  # None

# --- Default Arguments ---
def greet_with_time(name, time="morning"):
    print(f"Good {time}, {name}!")

greet_with_time("Amit")  # Uses default morning
greet_with_time("Amit", "evening")

# --- Keyword Arguments ---
def introduce(name, age, city):
    print(f"{name}, {age} years, from {city}")

introduce(age=21, name="Ravi", city="Belagavi")  # Order doesn't matter!

# --- *args & **kwargs (Important!) ---
# *args = multiple positional arguments as tuple
def sum_all(*args):
    print(f"args type: {type(args)}, value: {args}")
    return sum(args)

print(sum_all(1,2,3))
print(sum_all(10,20,30,40))

# **kwargs = multiple keyword arguments as dict
def print_profile(**kwargs):
    print(f"kwargs: {kwargs}")
    for key, val in kwargs.items():
        print(f"{key}: {val}")

print_profile(name="Anil", age=22, city="Pune", job="Dev")

# --- Scope: LEGB Rule ---
# Local, Enclosing, Global, Built-in
x = 100  # Global

def demo_scope():
    x = 10  # Local - shadows global
    print(f"Inside function x={x}")

demo_scope()
print(f"Outside x={x}")  # Global remains 100

# To modify global inside function, use global keyword (avoid if possible)
count = 0
def increment():
    global count
    count += 1

increment()
print(f"count {count}")

# --- Docstring ---
def area_of_circle(radius):
    """
    Calculate area of circle.
    
    Args:
        radius (float): Radius of circle
    
    Returns:
        float: Area
    """
    import math
    return math.pi * radius * radius

print(help(area_of_circle))  # Shows docstring
print(area_of_circle(5))

# --- EXERCISES ---
# 1. Write function is_prime(n) -> True if prime, else False
# 2. Write function factorial(n)
# 3. Write function to find max of 3 numbers
# 4. Write function that returns both area and circumference of circle (hint: return tuple)
# 5. Write function count_case(s) that returns count of upper and lower case letters: "Hello World" -> (1 upper, 9 lower? actually H,W upper)
