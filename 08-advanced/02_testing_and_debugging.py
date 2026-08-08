"""
TOPIC: Testing, Debugging, Logging
"""

# --- Debugging with print ---
def add(a,b):
    print(f"DEBUG: add called with a={a}, b={b}")  # Simple debug
    return a+b

# Better: using logging
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
# logging.debug, info, warning, error, critical

def divide(a,b):
    logging.info(f"Dividing {a} by {b}")
    if b == 0:
        logging.error("Division by zero attempted!")
        return None
    result = a/b
    logging.info(f"Result {result}")
    return result

divide(10,2)
divide(10,0)

# --- Assertions for testing ---
def factorial(n):
    assert isinstance(n, int), "n must be int"
    assert n >= 0, "n must be >=0"
    if n == 0:
        return 1
    return n * factorial(n-1)

print(f"factorial 5 {factorial(5)}")
# factorial(-1)  # AssertionError

# --- Unit Test with unittest ---
import unittest

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

class TestPrime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
    def test_not_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

# Run tests
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrime)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

# --- EXERCISES ---
# 1. Write function add with logging debug level, test with logging
# 2. Write unittest for your calculator functions
