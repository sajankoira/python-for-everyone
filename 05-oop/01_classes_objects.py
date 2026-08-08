"""
TOPIC: OOP - Classes & Objects
WHAT: Object Oriented Programming - Organize code like real world
Think: Class = Blueprint, Object = House built from blueprint
"""

# --- Class Definition ---
class Dog:
    # Class attribute - shared by all objects
    species = "Canis familiaris"

    # __init__ = Constructor - called when object created
    def __init__(self, name, age):
        # Instance attributes - unique to each object
        self.name = name
        self.age = age
        print(f"Dog object created: {name}")

    # Method - function inside class
    def bark(self):
        return f"{self.name} says Woof!"

    def get_age_human_years(self):
        return self.age * 7

# Creating Objects (Instantiation)
dog1 = Dog("Bruno", 3)
dog2 = Dog("Sheru", 5)

print(f"{dog1.name} is {dog1.age} years")
print(f"{dog2.name} is {dog2.age} years")
print(f"Species of all dogs: {Dog.species}")  # Access via class
print(f"Species via object: {dog1.species}")

print(dog1.bark())
print(f"{dog1.name} is {dog1.get_age_human_years()} in human years")

# --- Another Example: Bank Account ---
class BankAccount:
    def __init__(self, account_no, holder_name, balance=0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance {self.balance}")
        else:
            print("Amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance {self.balance}")
        else:
            print("Insufficient funds!")

    def __str__(self):  # Magic method for print(object)
        return f"Account {self.account_no} - {self.holder_name}: Balance {self.balance}"

# Use it
acc1 = BankAccount("123456", "Amit Sharma", 1000)
print(acc1)
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(2000)

# --- Understanding self ---
# self refers to current object calling the method
# When you do dog1.bark(), Python does Dog.bark(dog1) internally

# --- EXERCISES ---
# 1. Create class Student with name, roll_no, marks. Add method get_grade()
#    >90 A, >75 B, >60 C else D
# 2. Create class Rectangle with length, width, methods area(), perimeter()
# 3. Create class Book with title, author, price. Add __str__ method
# 4. What is difference between class attribute and instance attribute? Give example
