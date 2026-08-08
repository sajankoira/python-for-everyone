"""
TOPIC: File Handling & Exception Handling
"""

# --- Writing to File ---
# 'w' = write (overwrite), 'a' = append, 'r' = read

# Writing
f = open("demo.txt", "w")
f.write("Hello World!\n")
f.write("Learning Python file handling\n")
f.close()  # Always close! Or data may not save

# Better way: using 'with' - auto closes!
with open("demo.txt", "w") as f:
    f.write("Line 1 with with\n")
    f.write("Line 2 safe!\n")

# Append
with open("demo.txt", "a") as f:
    f.write("This is appended, not overwritten\n")

# Reading
with open("demo.txt", "r") as f:
    content = f.read()  # Reads entire file
    print("--- Full content ---")
    print(content)

with open("demo.txt", "r") as f:
    lines = f.readlines()  # List of lines
    print(f"\n--- As lines list ---\n{lines}")

with open("demo.txt", "r") as f:
    print("\n--- Line by line loop ---")
    for line in f:
        print(line.strip())  # strip removes \n

# Check if file exists
import os
print(f"\nFile exists? {os.path.exists('demo.txt')}")

# --- Working with JSON (Very Important for real world) ---
import json

data = {
    "name": "Amit",
    "age": 21,
    "skills": ["Python", "Git", "SQL"],
    "is_student": True
}

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # indent for pretty print

# Read JSON
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(f"\nLoaded JSON: {loaded}")
    print(f"Name from JSON: {loaded['name']}")

# --- Exception Handling ---
print("\n--- Exception Handling ---")

# Without try-except, program crashes!
try:
    # Risky code
    num = int(input("Enter number (try 'abc' to see error): ") or "10")  # default 10 if no input for demo
    result = 100 / num
    print(f"100 / {num} = {result}")
except ValueError:
    print("ValueError: That was not a valid number!")
except ZeroDivisionError:
    print("ZeroDivisionError: Can't divide by zero!")
except Exception as e:  # Catch all other errors
    print(f"Some other error: {e}")
else:
    print("No error occurred! Else block runs.")
finally:
    print("Finally always runs - good for cleanup!")

# Raising custom exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise Exception("Must be 18+ to vote")
    return True

try:
    validate_age(25)
    print("\nAge valid!")
    validate_age(-5)
except ValueError as ve:
    print(f"Validation error: {ve}")
except Exception as e:
    print(f"Other validation error: {e}")

# --- CSV Handling (Bonus) ---
import csv

# Write CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Amit", 21, "Belagavi"])
    writer.writerow(["Priya", 22, "Pune"])

# Read CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Cleanup demo files (optional)
# os.remove("demo.txt")
# os.remove("data.json")
# os.remove("students.csv")

# --- EXERCISES ---
# 1. Write program that counts words in a file
# 2. Create to-do app that saves tasks to file and loads on start
# 3. Try to open non-existing file and handle FileNotFoundError gracefully
# 4. Create JSON file of 3 students, then read and print student with highest marks
