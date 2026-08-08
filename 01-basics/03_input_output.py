"""
TOPIC: Input and Output
WHAT: Taking input from user and showing formatted output
WHY: Real programs interact with users!
"""

# --- CONCEPT 1: Taking Input ---
# input() always returns a STRING, even if user types number!

print("--- Let's take input ---")
# Uncomment below to try interactively:
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# age_str = input("Enter your age: ")
# print(f"You typed {age_str}, type is {type(age_str)}")

# --- CONCEPT 2: Type Casting (Converting Types) ---
# If you need number, convert it!

age_str = "21"  # Imagine this came from input()
age_int = int(age_str)  # Convert string to int
print(f"String '{age_str}' -> Int {age_int}")

height_str = "5.9"
height_float = float(height_str)
print(f"String '{height_str}' -> Float {height_float}")

number = 100
number_str = str(number)  # Int to String
print(f"Int {number} -> String '{number_str}'")

# Real example:
# In real code:
# age = int(input("Enter your age: "))
# print(f"Next year you will be {age + 1}")

# --- CONCEPT 3: Formatted Output - 3 Ways ---
name = "Priya"
marks = 92
city = "Belagavi"

# Method 1: Comma separation (adds space automatically)
print("Method 1:", "My name is", name, "and I scored", marks)

# Method 2: .format() method (old but still seen)
print("Method 2: My name is {} and I scored {} from {}".format(name, marks, city))

# Method 3: f-string (BEST, modern, fastest) - USE THIS!
print(f"Method 3: My name is {name} and I scored {marks} from {city}")

# f-strings can do calculations inside!
a = 10
b = 5
print(f"{a} + {b} = {a+b}")
print(f"{a} * {b} = {a*b}")

# Formatting numbers
pi = 3.1415926535
print(f"Pi is approx {pi:.2f}")  # .2f = 2 decimal places

# --- CONCEPT 4: Escape Characters ---
print("\n--- Escape Characters ---")
print("Line 1\nLine 2")  # \n = new line
print("Name:\tJohn")     # \t = tab
print("He said \"Python is awesome\"")  # \" to print quote
print('It\'s a beautiful day')   # \' to print single quote
print("Path: C:\\Users\\Python") # \\ to print backslash

# --- EXERCISES ---
# 1. Ask user: name, age, favorite hobby. Then print: "Hi NAME, at AGE, it's great you like HOBBY"
#    Remember to handle input() if running script
# 2. Take two numbers as input, convert to int, print their sum
#    Example: num1 = int(input("Enter first number: "))
# 3. Take your name and print a greeting with 3 different formatting methods
# 4. Print this exactly using escapes: 
#    He said, "C:\new\folder is my path" 
#    Next line with tab

print("\n--- Practice Solution Demo (non-interactive) ---")
# Simulating input for demo
sim_name = "Alex"
sim_age = 22
sim_hobby = "Coding"
print(f"Hi {sim_name}, at {sim_age}, it's great you like {sim_hobby}!")

# Exercise 2 demo
num1, num2 = 15, 25  # imagine these came from int(input())
print(f"Sum of {num1} and {num2} is {num1+num2}")

# Exercise 4
print("He said, \"C:\\new\\folder is my path\"")
print("Line one\n\tLine two with tab")
