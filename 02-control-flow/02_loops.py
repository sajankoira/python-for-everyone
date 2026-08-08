"""
TOPIC: Loops - Repeat without Repeating Yourself
WHAT: for loop & while loop
WHY: Don't write print 100 times, loop it!
"""

# --- FOR LOOP: Used when you know how many times ---
print("--- For Loop ---")

# 1. Loop over range
for i in range(5):  # 0 to 4 (5 not included)
    print(i)

print("---")
for i in range(1, 6):  # 1 to 5
    print(i)

print("--- Step ---")
for i in range(0, 10, 2):  # start, stop, step
    print(i)  # 0,2,4,6,8

# 2. Loop over string
name = "Python"
for char in name:
    print(char)

# 3. Loop with else (unique to Python!)
for i in range(3):
    print(i)
else:
    print("Loop finished - else executed!")

# --- WHILE LOOP: Used when condition based ---
print("\n--- While Loop ---")
count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1  # Very important! Otherwise infinite loop!

# --- LOOP Control: break, continue, pass ---
print("\n--- Break & Continue ---")

# break: Exit loop completely
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0-4 then stops

print("---")

# continue: Skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Prints only odd 1,3,5,7,9

# pass: Does nothing, placeholder
for i in range(3):
    pass  # TODO: will implement later
print("Pass does nothing, just avoids error")

# --- Nested Loops ---
print("\n--- Nested Loops: Multiplication Table ---")
for i in range(1, 4):  # Tables 1 to 3
    for j in range(1, 6):  # 1 to 5
        print(f"{i} x {j} = {i*j}")
    print("---")

# --- Real World Examples ---

# Sum of first n numbers
n = 10
total = 0
for i in range(1, n+1):
    total += i
print(f"Sum of 1 to {n} = {total}")

# Factorial using while
num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(f"Factorial of {num} = {fact}")

# --- EXERCISES ---
# 1. Print numbers 1 to 100 but skip numbers divisible by 3
# 2. Print multiplication table of any number (take input)
# 3. Count how many vowels in a string: "Belagavi is awesome"
# 4. Guess the number game: while user guess != secret, keep asking
# 5. Print pattern:
#    *
#    **
#    ***
#    ****

print("\n--- Exercise 3 Demo: Count Vowels ---")
text = "Belagavi is awesome".lower()
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Vowels in '{text}' = {count}")

# Exercise 5 Demo
print("\n--- Pattern ---")
for i in range(1, 6):
    print("*" * i)
