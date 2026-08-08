"""
TOPIC: Lambda, Map, Filter, Recursion
"""

# --- Lambda: Anonymous small function ---
# Syntax: lambda args: expression

# Normal function:
def square_old(n):
    return n*n

# Lambda:
square = lambda n: n*n
print(square(5))

add = lambda a,b: a+b
print(add(3,4))

# When used? Short function for map/filter/sort

# --- Map: Apply function to each item ---
nums = [1,2,3,4,5]
squared = list(map(lambda x: x*x, nums))
print(f"map square: {squared}")

# Without lambda:
def to_str(n):
    return str(n)
str_nums = list(map(to_str, nums))
print(str_nums)

# --- Filter: Keep items where condition True ---
evens = list(filter(lambda x: x%2==0, nums))
print(f"filter evens: {evens}")

# --- Sorted with key ---
students = [("Amit", 85), ("Priya", 92), ("Rahul", 78)]
# Sort by marks
sorted_by_marks = sorted(students, key=lambda x: x[1])  # x[1] is marks
print(f"Sorted by marks: {sorted_by_marks}")

# --- List Comprehension vs Map/Filter ---
# Generally comprehension is more Pythonic
squares_comp = [x*x for x in nums]
evens_comp = [x for x in nums if x%2==0]
print(f"Comp squares: {squares_comp}, evens: {evens_comp}")

# --- Recursion: Function calls itself ---
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(f"factorial 5: {factorial(5)}")

# Fibonacci recursion (inefficient but educational)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(f"fib 6: {fib(6)}")  # 0,1,1,2,3,5,8...

# --- Decorators (Brief Intro) ---
# Decorator modifies behavior of function without changing code
def my_decorator(func):
    def wrapper():
        print("Something before function")
        func()
        print("Something after function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# --- EXERCISES ---
# 1. Use map to convert list of string numbers ["1","2","3"] to ints
# 2. Use filter to get words with length > 5 from ["Python","is","awesome","programming"]
# 3. Write recursive function to sum list: sum_list([1,2,3]) -> 6
# 4. Write lambda to check if number is even: is_even = lambda x: x%2==0
