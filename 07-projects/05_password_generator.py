"""
PROJECT 5: Password Generator
"""
import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Ensure at least one of each selected type
    password = []
    password.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*"))

    # Fill rest
    for _ in range(length - len(password)):
        password.append(random.choice(chars))

    random.shuffle(password)
    return "".join(password)

def strength_check(pwd):
    score = 0
    if len(pwd) >= 8:
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*" for c in pwd):
        score += 1
    levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    return levels[min(score, 4)]

if __name__ == "__main__":
    print("🔐 Password Generator")
    length = int(input("Length (default 12): ") or 12)
    pwd = generate_password(length)
    print(f"Generated: {pwd}")
    print(f"Strength: {strength_check(pwd)}")
    # Generate 5 options
    print("\n5 options:")
    for i in range(5):
        print(f"{i+1}. {generate_password(length)}")
