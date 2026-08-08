"""
TOPIC: Strings Deep Dive
WHAT: Everything about text handling
"""

# --- String Basics ---
s = "Python"
print(f"String: {s}, Length: {len(s)}")

# Accessing characters (Indexing) 0-based
print(s[0])   # P
print(s[-1])  # n - last char
print(s[-2])  # o

# Slicing [start:stop:step]
print(s[0:4])   # Pyth (0 to 3)
print(s[:4])    # Same as above
print(s[2:])    # thon (2 to end)
print(s[::2])   # Pto (every 2nd char)
print(s[::-1])  # nohtyP (reverse!)

# Strings are Immutable - can't change
# s[0] = "J"  # Error! TypeError

# Create new string instead
new_s = "J" + s[1:]
print(new_s)  # Jython

# --- String Methods (Very Important!) ---
text = "  Hello Python World, Python is Great!  "

print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"strip(): '{text.strip()}' - removes spaces both sides")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")
print(f"replace(): '{text.replace('Python', 'Java')}'")
print(f"split(): {text.split()}")  # Splits by spaces into list
print(f"count('Python'): {text.count('Python')}")
print(f"find('Python'): {text.find('Python')}")  # Index or -1 if not found
print(f"startswith('  Hello'): {text.startswith('  Hello')}")

# Join: opposite of split
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print(f"join(): {joined}")

# Check
print(f"'Python' in text? {'Python' in text}")

# --- f-string advanced ---
name = "Aisha"
age = 21
print(f"{name} is {age} years old")
print(f"{name.upper()} - next year {age+1}")
print(f"{{name}} prints braces: {name}")  # {{}} to print {}

# --- EXERCISES ---
# 1. Take a string, print reverse without using [::-1] (use loop)
# 2. Check if string is palindome: "madam", "racecar", "naman" -> same forward/backward
#    Ignore case and spaces: "Naman" -> True
# 3. Count words in sentence: "I love Python programming"
# 4. Take email "user@gmail.com" -> extract username "user" and domain "gmail.com" using split('@')
# 5. Clean this string: "  *** Hello!!! Python---  " -> "Hello Python"
