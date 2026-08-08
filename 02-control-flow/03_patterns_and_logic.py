"""
TOPIC: Pattern Printing & Logic Building
WHAT: Master loops by building patterns - asked in every interview!
"""

# Pattern 1: Right Triangle
print("--- Pattern 1: Right Triangle ---")
n = 5
for i in range(1, n+1):
    print("*" * i)

# Pattern 2: Inverted Triangle
print("\n--- Pattern 2: Inverted Triangle ---")
for i in range(n, 0, -1):
    print("*" * i)

# Pattern 3: Pyramid
print("\n--- Pattern 3: Pyramid ---")
for i in range(1, n+1):
    spaces = " " * (n - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

# Pattern 4: Number Triangle
print("\n--- Pattern 4: Number Triangle ---")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Pattern 5: Same Number Each Row
print("\n--- Pattern 5 ---")
for i in range(1, n+1):
    print((str(i) + " ") * i)

# Pattern 6: Multiplication Table Grid
print("\n--- Pattern 6: Grid ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# Pattern 7: Diamond (Advanced - combines two loops)
print("\n--- Pattern 7: Diamond ---")
# Upper half
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))
# Lower half
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))

# Logic Building: Armstrong, Prime, Palindrome
print("\n--- Logic Building ---")

# Armstrong: 153 = 1^3 + 5^3 + 3^3
num = 153
temp = num
digits = len(str(num))
sum_pow = 0
while temp > 0:
    digit = temp % 10
    sum_pow += digit ** digits
    temp //= 10
print(f"{num} Armstrong? {num == sum_pow}")

# Prime: divisible only by 1 and itself
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print(f"17 prime? {is_prime(17)}, 15 prime? {is_prime(15)}")

# --- EXERCISES ---
# 1. Print hollow square: 
#    *****
#    *   *
#    *   *
#    *****
# 2. Print Floyd's Triangle:
#    1
#    2 3
#    4 5 6
# 3. Find all Armstrong numbers 100-999
# Hint: loop 100-999 and check logic above
