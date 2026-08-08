"""
TOPIC: Dict & Set
DICT = key:value, mutable, unordered (insertion ordered since 3.7), keys unique
SET = unordered, unique elements
"""

# --- DICTIONARY ---
print("--- DICTIONARY ---")

student = {
    "name": "Rahul",
    "age": 21,
    "city": "Belagavi",
    "marks": 92,
    "is_passed": True
}

print(student)
print(f"Name: {student['name']}")  # Access via key
# print(student['grade'])  # KeyError if not exists

# Safe access with .get()
print(f"Grade (get): {student.get('grade', 'Not Found')}")

# Add/Update
student["grade"] = "A"  # Add new
student["marks"] = 95   # Update existing
print(f"After add/update: {student}")

# Remove
student.pop("is_passed")
print(f"After pop: {student}")

# Methods
print(f"\nKeys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")  # Key-value pairs

# Looping dict
print("\nLooping:")
for key in student:
    print(f"{key} -> {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")

# Nested dict
students = {
    "101": {"name": "Amit", "marks": 90},
    "102": {"name": "Priya", "marks": 95}
}
print(f"\nNested: {students['101']['name']}")

# Dict Comprehension
squares_dict = {x: x*x for x in range(1,6)}
print(f"Dict comprehension: {squares_dict}")

# --- SET ---
print("\n--- SET ---")

# Unordered collection of unique items
numbers = [1,2,2,3,3,3,4,5,5]
unique = set(numbers)
print(f"List {numbers} -> Set {unique}")

# Create set
my_set = {1,2,3}
print(my_set)

# empty set: must use set(), {} creates empty dict!
empty = set()
print(type(empty))

# Methods
my_set.add(4)
my_set.add(2)  # Duplicate ignored
print(f"After add: {my_set}")

my_set.remove(2)  # Error if not exists
my_set.discard(10)  # No error if not exists
print(f"After remove: {my_set}")

# Set operations - VERY useful!
A = {1,2,3,4,5}
B = {4,5,6,7,8}

print(f"\nA={A}, B={B}")
print(f"A union B: {A | B}")  # or A.union(B)
print(f"A intersection B: {A & B}")  # A.intersection(B) -> common
print(f"A difference B: {A - B}")  # In A not in B
print(f"A symmetric diff: {A ^ B}")  # Not common

# --- Real World Examples ---

# Word frequency counter
sentence = "python is great and python is fun"
freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1
print(f"\nWord freq: {freq}")

# Remove duplicates but keep order (Python 3.7+ dict keeps order)
items = ["apple", "banana", "apple", "mango", "banana"]
unique_ordered = list(dict.fromkeys(items))
print(f"Unique ordered: {unique_ordered}")

# --- EXERCISES ---
# 1. Create dict of 3 students: roll_no -> {name, marks}. Print student with highest marks
# 2. Merge two dicts: d1={"a":1,"b":2}, d2={"b":3,"c":4} -> {"a":1,"b":3,"c":4} (Python 3.9+ use |)
# 3. Check if two strings are anagrams using dict/counter: "listen" & "silent" -> True
# 4. Set: Given list, find duplicates using set logic
# 5. Inventory: Store items with quantity, allow add/remove/print low stock <5
