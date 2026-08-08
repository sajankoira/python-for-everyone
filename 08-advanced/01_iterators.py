"""
TOPIC: Advanced - Iterators, Generators, Comprehensions
"""
# List comprehension with condition + nested
nums = [1,2,3,4,5,6]
evens_squared = [x*x for x in nums if x%2==0]
print(evens_squared)

# Dict comprehension
word = "belagavi"
freq = {c: word.count(c) for c in set(word)}
print(freq)

# Generator memory demo
import sys
list_big = [x for x in range(10000)]
gen_big = (x for x in range(10000))
print(f"List size: {sys.getsizeof(list_big)} bytes")
print(f"Generator size: {sys.getsizeof(gen_big)} bytes - much smaller!")

# Iterator chaining
# Read large file lazily
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

# Simulated
print("Iterator chaining example: filter even squares")
result = (x*x for x in range(20) if x%2==0)
print(list(result))
