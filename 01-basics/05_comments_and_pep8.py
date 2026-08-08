"""
TOPIC: Comments, Docstrings & PEP8 (Clean Code)
WHAT: How to write readable code that others love
WHY: Code is read 10x more than it's written. Your future self will thank you!
"""

# This is a single line comment - use for quick notes

# TODO: This is a convention to mark something to be done later
# FIXME: Mark something that needs fixing

"""
This is a multi-line comment / docstring.
Docstrings are special - they DOCUMENT your code.
When you put triple quotes right after def or class or at top of file,
it becomes documentation!
"""

# --- PEP8: Python's Style Guide (Very Important!) ---
# Official guide: https://peps.python.org/pep-0008/

# 1. Use snake_case for variables and functions
# GOOD
student_name = "Amit"
total_marks = 95

# BAD (don't do)
StudentName = "Amit"  # This is for Classes
totalMarks = 95       # This is camelCase - JS style, not Python

# 2. Use 4 spaces for indentation (not tabs)
# Python cares about indentation!
if True:
    print("This is indented with 4 spaces")
    print("This also")

# 3. Keep lines under 79 characters
# Instead of super long line:
# result = very_long_variable_name_one + very_long_variable_name_two + very_long_variable_name_three
# Do this:
result = (
    10 + 20 + 30 + 
    40 + 50
)

# 4. Use spaces around operators
# GOOD
x = 5 + 3
y = 10

# BAD
# x=5+3

# 5. Two blank lines before function definitions (we'll learn functions soon)
# One blank line between logical sections

# --- Good Example of Well-Documented Code ---
def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Formula: SI = (P * R * T) / 100

    Args:
        principal (float): Initial amount
        rate (float): Rate of interest per year
        time (float): Time in years

    Returns:
        float: Simple interest
    """
    # Validate inputs are positive
    if principal <= 0 or rate <= 0 or time <= 0:
        return 0
    
    # Calculate interest
    interest = (principal * rate * time) / 100
    return interest


# Using the function
p = 10000
r = 5
t = 2
si = calculate_simple_interest(p, r, t)
print(f"Simple Interest for P={p}, R={r}%, T={t} years is {si}")

# --- EXERCISES ---
# 1. Write a poorly written code snippet then rewrite it in PEP8 style
# 2. Add proper docstring to a function that calculates area of circle: pi*r^2
# 3. Install a linter: pip install flake8 and run flake8 on your file to check style
#    (Optional - we'll cover pip later)
