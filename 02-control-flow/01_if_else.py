"""
TOPIC: If-Else - Making Decisions
WHAT: Run different code based on conditions
WHY: Life is decision making! If it's raining, take umbrella else go normally.
"""

# --- SYNTAX ---
# if condition:
#     code if True
# elif another_condition:
#     code
# else:
#     code if none True

# --- EXAMPLE 1: Simple if ---
age = 18
if age >= 18:
    print("You can vote!")

# --- EXAMPLE 2: if-else ---
age = 16
if age >= 18:
    print("You can vote!")
else:
    print(f"Wait {18-age} more years!")

# --- EXAMPLE 3: if-elif-else Ladder ---
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Marks {marks} -> Grade {grade}")

# --- EXAMPLE 4: Nested If ---
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful!")
    else:
        print("Wrong password!")
else:
    print("Unknown user")

# --- EXAMPLE 5: Ternary Operator - Short if-else ---
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# --- COMMON MISTAKE: Indentation ---
# Python uses indentation to know which code belongs to if!
# This will error:
# if True:
# print("No indent")  # IndentationError

# --- Falsy Values (Important!) ---
# In Python, these are considered False: 0, 0.0, "", [], {}, None, False
# Everything else is True!

print("\n--- Truthy/Falsy Demo ---")
if 0:
    print("0 is Truthy")
else:
    print("0 is Falsy")  # This prints

if "Hello":
    print("'Hello' is Truthy")  # This prints

if "":
    print("empty string truthy")
else:
    print("empty string is Falsy")

# --- EXERCISES ---
# 1. Take age as input, print: Child (<13), Teen (13-19), Adult (20-59), Senior (60+)
# 2. Check if number is positive, negative, or zero
# 3. Take 3 numbers, find the largest without using max()
# 4. Simple login system: if username=="student" and password=="python123" print success else fail
# 5. Check if year is leap year: divisible by 4 and (not divisible by 100 unless divisible by 400)
#    Example: 2000 leap, 1900 not leap, 2024 leap

print("\n--- Demo Exercises ---")
# 1
age = 25
if age < 13:
    cat = "Child"
elif age <= 19:
    cat = "Teen"
elif age <= 59:
    cat = "Adult"
else:
    cat = "Senior"
print(f"Age {age} -> {cat}")

# 2
num = -5
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("Zero")
