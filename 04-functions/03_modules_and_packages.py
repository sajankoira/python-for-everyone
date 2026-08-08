"""
TOPIC: Modules, Packages, pip and virtualenv - How real Python projects work
"""

# --- What is Module? ---
# Any .py file is a module! You can import it.

# Example 1: Using built-in modules
import math
import random
import datetime

print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.pi = {math.pi}")
print(f"random number 1-100: {random.randint(1,100)}")
print(f"random choice from list: {random.choice(['apple','banana','mango'])}")
print(f"Today: {datetime.date.today()}")

# Import specific things
from math import pi, factorial
print(f"pi = {pi}, factorial 5 = {factorial(5)}")

# Alias
import datetime as dt
print(f"Now with alias: {dt.datetime.now()}")

# --- Creating Your Own Module ---
# Suppose we have file my_math.py:
# def add(a,b): return a+b
# def mul(a,b): return a*b
# You can then: import my_math; my_math.add(2,3)

# Let's simulate:
# Write a module file dynamically (demo)
with open("my_custom_module.py", "w") as f:
    f.write("""
def greet(name):
    return f"Hello {name} from custom module!"

PI = 3.14159

def circle_area(r):
    return PI * r * r
""")

# Now import it
import my_custom_module
print(my_custom_module.greet("Sajan"))
print(f"Area r=5: {my_custom_module.circle_area(5)}")

# --- Packages ---
# Package = Folder with __init__.py file containing modules
# Example:
# mypackage/
#   __init__.py
#   math_tools.py
#   string_tools.py
# You import as: from mypackage import math_tools

# --- pip: Python's package manager ---
# pip installs external libraries created by others

# Common commands (run in terminal, not here):
# pip install requests        # For API calls
# pip install pandas matplotlib   # For Data Science
# pip install flask           # For web apps
# pip install --upgrade pip
# pip list                    # Show installed
# pip freeze > requirements.txt   # Save dependencies

# Demo using requests (if installed)
try:
    import requests
    print("requests is installed! Version:", requests.__version__)
    # response = requests.get("https://api.github.com")
    # print(response.status_code)
except ImportError:
    print("requests not installed. Install with: pip install requests")

# --- virtualenv: Isolate project dependencies ---
# Why needed? Project A needs pandas 1.0, Project B needs pandas 2.0. Conflict!
# Solution: virtualenv creates separate folders per project.

# Commands:
# python -m venv venv          # Create venv folder
# source venv/bin/activate      # Activate on Linux/Mac
# venv\Scripts\activate         # Activate on Windows
# deactivate                    # Exit venv
# After activation, pip install installs only inside venv, not system-wide

# --- __name__ == "__main__" Trick ---
# When you import a file, all top-level code runs!
# To prevent that, use:
# if __name__ == "__main__":
#     # This code runs ONLY when file executed directly
#     # Not when imported
#     main()

print(f"\n__name__ is {__name__}")
# In this file, __name__ = "__main__" when you run python this_file.py
# If imported, __name__ = "03_modules_and_packages"

# --- EXERCISES ---
# 1. Create your own module calculator.py with add, sub, mul, div functions
#    Then import and use it in another file
# 2. Install requests: pip install requests, then write script to get weather of Belagavi using API
# 3. Create a package called mytools with 2 modules: text.py (reverse string, count words) and numbers.py (is_prime, factorial)
# 4. Create venv and install pandas, try import pandas
