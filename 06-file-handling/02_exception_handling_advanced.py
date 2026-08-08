"""
TOPIC: Exception Handling - Advanced + Custom Exceptions
"""

# Built-in exceptions: ZeroDivisionError, ValueError, TypeError, IndexError, KeyError, FileNotFoundError, etc

# --- Multiple except + else + finally ---
try:
    a = int(input("Enter number: ") or "10")
    b = int(input("Enter divisor: ") or "2")
    result = a / b
    print(f"{a}/{b}={result}")
except ValueError as ve:
    print(f"ValueError: Enter valid int. Details: {ve}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("Else: No exception, success!")
    # Good place to run code only if no error
finally:
    print("Finally: Always runs, cleanup here")
    # Close files, DB connections, etc

# --- Raising Custom Exception ---
class AgeTooLowError(Exception):
    """Custom exception for voting"""
    pass

def check_voting_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise AgeTooLowError(f"Age {age} is below 18, cannot vote")
    return True

tests = [15, 20, -5]
for age in tests:
    try:
        check_voting_age(age)
        print(f"Age {age} can vote")
    except AgeTooLowError as e:
        print(f"Custom error: {e}")
    except ValueError as ve:
        print(f"ValueError: {ve}")

# --- Exception Chaining ---
try:
    try:
        x = int("abc")
    except ValueError as ve:
        raise TypeError("Failed to parse, type issue") from ve
except TypeError as te:
    print(f"Chained exception: {te}, cause: {te.__cause__}")

# --- Best Practices ---
# 1. Don't do bare except:  try: ... except: ...   # Bad, hides bugs
# 2. Catch specific exceptions
# 3. Keep try block small - only risky code
# 4. Use finally for cleanup, or better use 'with' statement
# 5. Log exceptions in real projects: import logging; logging.error(e)

# --- Context Manager with 'with' (auto handles exceptions/cleanup) ---
# with open() is context manager. You can create own:

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Exception {exc_type} handled")
        return False  # False = don't suppress exception

print("\n--- Custom Context Manager ---")
try:
    with FileManager("temp_demo.txt", "w") as f:
        f.write("Hello via context manager\n")
    with FileManager("temp_demo.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

# Cleanup
import os
if os.path.exists("temp_demo.txt"):
    os.remove("temp_demo.txt")
if os.path.exists("my_custom_module.py"):
    os.remove("my_custom_module.py")
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
if os.path.exists("data.json"):
    os.remove("data.json")
if os.path.exists("students.csv"):
    os.remove("students.csv")
if os.path.exists("todo.json"):
    os.remove("todo.json")

# --- EXERCISES ---
# 1. Write function safe_divide(a,b) that returns result or "Error: ..." string, never crashes
# 2. Create custom exception InsufficientBalanceError for BankAccount withdraw
# 3. Use try-except to handle file reading, if file not exists, create it with default content
