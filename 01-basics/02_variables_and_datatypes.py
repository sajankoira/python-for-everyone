"""
TOPIC: Variables & Data Types
WHAT: Variables are like boxes that store data
WHY: Programs need to remember things - your name, age, price, etc.

Think of Variable as: 
    Label on a box = variable name
    Thing inside box = value
"""

# --- CONCEPT 1: Creating Variables ---
# Syntax: variable_name = value
# No need to declare type, Python figures it out!

name = "Arjun"           # String (text) - always in quotes ""
age = 21                 # Integer (whole number)
height = 5.9             # Float (decimal number)
is_student = True        # Boolean - True or False (capital T/F)
# Python is case-sensitive: age and Age are different!

print(name, age, height, is_student)

# --- CONCEPT 2: Data Types Deep Dive ---
# Check type of variable using type() function

print("\n--- Types ---")
print("name type:", type(name))        # <class 'str'>
print("age type:", type(age))          # <class 'int'>
print("height type:", type(height))    # <class 'float'>
print("is_student type:", type(is_student))  # <class 'bool'>

# Other important types we'll see later:
# list, dict, tuple - for collections

# --- CONCEPT 3: Variable Naming Rules ---
# ✅ GOOD:
# my_name = "John"
# age2 = 25
# _private = "secret"
# total_marks = 98  # snake_case is pythonic!

# ❌ BAD:
# 2age = 25        # cannot start with number
# my-name = "John" # cannot use hyphen
# class = "10th"   # cannot use reserved keyword

# Python Reserved Keywords: if, for, while, class, def, True, False, etc.

# --- CONCEPT 4: Reassigning & Dynamic Typing ---
x = 10
print("\n x =", x, "type:", type(x))
x = "Now I am a string!"  # Same variable, different type! Allowed in Python
print(" x =", x, "type:", type(x))

# --- CONCEPT 5: Multiple Assignment ---
a, b, c = 1, 2, 3
print(a, b, c)

p = q = r = 0  # All three become 0
print(p, q, r)

# --- EXERCISES ---
print("\n--- Exercises: Try these! ---")
# 1. Create variables: your_name, your_city, your_favorite_language, year_you_started_learning = 2026
# 2. Print them using f-string: f"My name is {your_name} and I live in {your_city}"
# 3. Create two numbers num1=50, num2=10, then print their sum, difference, product
# 4. What happens if you do: name = "YourName" then name = 100 ? Try it!

# --- SOLUTION to Exercise 2 (Example) ---
your_name = "Learner"
your_city = "Belagavi"
your_favorite_language = "Python"
year_started = 2026

# f-string is the BEST way to print variables inside text (Python 3.6+)
print(f"My name is {your_name} and I live in {your_city}. I love {your_favorite_language}!")
print(f"I started learning in {year_started}")

# --- COMMON MISTAKE ---
# print(Name)  # Error if you did name = "Arjun" (capital N matters)
# print(age)   # Works
# print(agee)  # Typo -> NameError

# --- INTERVIEW TIP ---
# Q: What is dynamic typing?
# A: In Python, you don't need to declare variable type. Type is decided at runtime and can change.
