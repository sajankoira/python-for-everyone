"""
TOPIC: Operators in Python
WHAT: Symbols that perform operations on values
WHY: You need to calculate, compare, and make decisions
"""

# --- 1. Arithmetic Operators ---
a = 10
b = 3
print("--- Arithmetic ---")
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")   # Addition
print(f"a - b = {a - b}")   # Subtraction
print(f"a * b = {a * b}")   # Multiplication
print(f"a / b = {a / b}")   # Division (always gives float)
print(f"a // b = {a // b}")  # Floor Division (removes decimal)
print(f"a % b = {a % b}")   # Modulo (remainder) - VERY IMPORTANT!
print(f"a ** b = {a ** b}")  # Exponentiation (Power) 10^3

# Real use of %: Check even/odd
num = 10
print(f"\n{num} % 2 = {num % 2} -> Even if 0, Odd if 1")

# --- 2. Comparison Operators (Result is always True/False) ---
print("\n--- Comparison ---")
x, y = 10, 20
print(f"x == y: {x == y}")  # Equal to
print(f"x != y: {x != y}")  # Not equal to
print(f"x > y: {x > y}")    # Greater than
print(f"x < y: {x < y}")    # Less than
print(f"x >= y: {x >= y}")  # Greater than or equal
print(f"x <= y: {x <= y}")  # Less than or equal

# --- 3. Assignment Operators (Shorthand) ---
print("\n--- Assignment ---")
n = 5
print(f"n = {n}")
n += 2  # Same as n = n + 2
print(f"n += 2 -> {n}")
n -= 1  # n = n - 1
print(f"n -= 1 -> {n}")
n *= 3  # n = n * 3
print(f"n *= 3 -> {n}")
n /= 2
print(f"n /= 2 -> {n}")

# --- 4. Logical Operators (and, or, not) ---
print("\n--- Logical ---")
# Think in real life:
has_passport = True
has_ticket = False

print(f"has_passport and has_ticket: {has_passport and has_ticket}")  # Both must be True
print(f"has_passport or has_ticket: {has_passport or has_ticket}")    # At least one True
print(f"not has_ticket: {not has_ticket}")  # Inverts

# Example: Eligibility
age = 20
has_id = True
can_vote = (age >= 18) and has_id
print(f"Age {age}, has_id {has_id}, can_vote: {can_vote}")

# --- 5. Membership Operators (in, not in) ---
print("\n--- Membership ---")
text = "Python is awesome"
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'Java' not in text: {'Java' not in text}")

# Works with lists too (we will learn later)
my_list = [1, 2, 3, 4]
print(f"3 in my_list: {3 in my_list}")

# --- 6. Identity Operators (is, is not) - Advanced ---
# Don't worry too much now, just know difference between == and is
print("\n--- Identity (== vs is) ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 == list2: {list1 == list2}")  # Values equal? Yes
print(f"list1 is list2: {list1 is list2}")  # Same object in memory? No
print(f"list1 is list3: {list1 is list3}")  # Same object? Yes, because list3 = list1

# --- EXERCISES ---
print("\n--- Exercises ---")
# 1. Take two numbers: calculate area of rectangle if they are length and breadth
# 2. Convert Celsius to Fahrenheit: F = (C * 9/5) + 32. Try C=37
# 3. Check if a number is divisible by both 3 and 5 (hint: use % and and)
#    Example: num=15 -> Hint: num%3==0 and num%5==0
# 4. Swap two numbers without third variable using arithmetic? (Research!)
# 5. Take a string and check if letter 'a' is in it (case-insensitive)

# --- Solutions ---
print("\nSolutions Demo:")
# 2.
c = 37
f = (c * 9/5) + 32
print(f"{c}C = {f}F")

# 3.
num = 15
print(f"{num} divisible by 3 and 5? {num % 3 == 0 and num % 5 == 0}")

# 5.
s = "Belagavi"
print(f"'a' in '{s}' (lowercase)? {'a' in s.lower()}")
