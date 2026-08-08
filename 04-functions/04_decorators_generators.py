"""
TOPIC: Advanced Functions - Decorators, Generators, Iterators
"""

# --- Generator: Function that yields, not returns ---
# Return gives all at once, uses memory. Generator yields one at a time!

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(5)
print("Generator:", gen)
for num in gen:
    print(num)

# Why generator? For large data: range(1000000) is generator-like, doesn't store all numbers
print(f"Sum of generator: {sum(count_up_to(100))}")

# List vs Generator expression
list_comp = [x*x for x in range(10)]  # List, stores all
gen_exp = (x*x for x in range(10))     # Generator, lazy
print(f"List: {list_comp}, Generator: {gen_exp}, Sum gen: {sum(gen_exp)}")

# Fibonacci generator
def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

print(f"Fib 10: {list(fib_gen(10))}")

# --- Decorator: Modify function without changing its code ---

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello {name}!")
    return f"Greeted {name}"

print("\n--- Decorator Demo ---")
val = say_hello("Sajan")
print(val)

# Practical decorator: Timing function
import time
import functools

def timer(func):
    @functools.wraps(func)  # Keeps original function name
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Slow work done")

slow_function()

# --- Iterator Protocol (Brief) ---
nums = [1,2,3]
it = iter(nums)  # Get iterator
print(f"\nIterator next: {next(it)}, {next(it)}, {next(it)}")
# next(it) again would error StopIteration

# Custom iterator class
class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

print("Countdown 5:")
for n in Countdown(5):
    print(n)

# --- EXERCISES ---
# 1. Write generator that yields even numbers up to n
# 2. Write decorator @debug that prints function name and args before calling
# 3. Write generator that reads large file line by line (don't load all at once)
