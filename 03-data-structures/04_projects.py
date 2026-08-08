"""
TOPIC: Data Structures - Real World Mini Projects
"""

# Project 1: Word Frequency + Most Common
sentence = "python is great and python is fun and python is easy"
words = sentence.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(f"Frequency: {freq}")
most_common = max(freq, key=freq.get)
print(f"Most common: {most_common} appears {freq[most_common]} times")

# Project 2: Inventory Management with Dict
inventory = {
    "apple": {"price": 100, "qty": 50},
    "banana": {"price": 40, "qty": 100},
    "mango": {"price": 120, "qty": 30}
}

def show_inventory(inv):
    print("\n--- Inventory ---")
    for item, data in inv.items():
        print(f"{item}: Rs.{data['price']} x {data['qty']} = Rs.{data['price']*data['qty']}")

def low_stock(inv, threshold=40):
    return [item for item, data in inv.items() if data['qty'] < threshold]

show_inventory(inventory)
print(f"Low stock (<40): {low_stock(inventory)}")

# Project 3: Remove duplicates keeping order - using dict.fromkeys
items = ["apple", "banana", "apple", "mango", "banana", "orange"]
unique = list(dict.fromkeys(items))
print(f"\nOriginal: {items}")
print(f"Unique ordered: {unique}")

# Project 4: Anagram Checker (2 methods)
def is_anagram_dict(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for c in s1.lower():
        freq[c] = freq.get(c, 0) + 1
    for c in s2.lower():
        if c not in freq or freq[c] == 0:
            return False
        freq[c] -= 1
    return True

def is_anagram_sorted(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(f"\nlisten & silent anagram? dict method {is_anagram_dict('listen','silent')}, sorted method {is_anagram_sorted('listen','silent')}")

# Project 5: Second Largest without sort
nums = [10, 5, 8, 12, 3, 12]
largest = second = float('-inf')
for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n
print(f"\nList {nums} -> largest {largest}, second largest {second}")

# Project 6: Group Anagrams
from collections import defaultdict
words = ["eat","tea","tan","ate","nat","bat"]
groups = defaultdict(list)
for w in words:
    key = tuple(sorted(w))
    groups[key].append(w)
print(f"\nGroup anagrams {words} -> {list(groups.values())}")

# --- EXERCISES: Try these now ---
# 1. Students dict roll->{name,marks}: find topper, average marks
# 2. Merge 2 dicts without overwriting? Keep both values in list
# 3. Find common elements in 3 lists using set intersection
