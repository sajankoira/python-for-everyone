"""
TOPIC: Lists & Tuples
WHAT: Store many values together
LIST = Mutable, ordered, allows duplicates [1,2,3]
TUPLE = Immutable, ordered, allows duplicates (1,2,3)
"""

# --- LISTS ---
print("--- LISTS ---")
fruits = ["apple", "banana", "mango", "apple"]
print(fruits)
print(f"Length: {len(fruits)}")
print(f"First: {fruits[0]}, Last: {fruits[-1]}")

# Slicing same as strings
print(fruits[1:3])

# Mutable - can change
fruits[1] = "kiwi"
print(f"After change: {fruits}")

# Methods
# Add
fruits.append("orange")  # Add at end
print(f"append: {fruits}")

fruits.insert(1, "grapes")  # Insert at index
print(f"insert at 1: {fruits}")

# Remove
fruits.remove("apple")  # Removes first occurrence
print(f"remove apple: {fruits}")

popped = fruits.pop()  # Removes last and returns it
print(f"pop: {popped}, list now: {fruits}")

popped2 = fruits.pop(0)  # Remove at index 0
print(f"pop(0): {popped2}, list now: {fruits}")

# Other methods
nums = [3, 1, 4, 1, 5, 9, 2]
print(f"\nnums: {nums}")
print(f"count(1): {nums.count(1)}")
print(f"index(4): {nums.index(4)}")
nums.sort()
print(f"sort(): {nums}")
nums.reverse()
print(f"reverse(): {nums}")

# --- List Comprehension (Pythonic Magic!) ---
# Instead of:
squares_old = []
for i in range(5):
    squares_old.append(i*i)
print(f"\nSquares old way: {squares_old}")

# Do this:
squares = [i*i for i in range(5)]
print(f"Squares new way: {squares}")

evens = [i for i in range(10) if i % 2 == 0]
print(f"Evens: {evens}")

# --- Copying Lists - IMPORTANT! ---
# WRONG way
list1 = [1,2,3]
list2 = list1  # Both point same memory!
list2.append(4)
print(f"list1 after modifying list2: {list1} - oops!")

# CORRECT ways
list1 = [1,2,3]
list2 = list1.copy()
# or list2 = list1[:]
# or list2 = list(list1)
list2.append(4)
print(f"Correct copy - list1: {list1}, list2: {list2}")

print("\n--- TUPLES ---")
# Tuples are immutable lists
coords = (10, 20)
print(f"coords: {coords}, x={coords[0]}")

# Why use tuple?
# 1. Faster than list
# 2. Safe - can't accidentally change
# 3. Can be key in dict (list can't)
# 4. For fixed data: (lat, long), (x,y)

# Single element tuple needs comma!
single = (5,)  # Tuple
not_tuple = (5)  # Just int
print(type(single), type(not_tuple))

# Unpacking
x, y = (10, 20)
print(f"Unpacked x={x}, y={y}")

# Swapping with tuple
a, b = 5, 10
a, b = b, a
print(f"Swapped a={a}, b={b}")

# --- EXERCISES ---
# 1. Have list [1,2,3,2,4,2,5] remove all 2's
# 2. Find second largest number in list without sort(): [10,5,8,12,3] -> 10
# 3. Reverse a list without using reverse() or [::-1]
# 4. Create list of first 10 squares using list comprehension
# 5. Tuple (1,2,3) + (4,5) ? Try tuple concatenation
