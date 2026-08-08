"""
TOPIC: Advanced OOP - Magic Methods, Abstract Classes, Composition vs Inheritance
"""

# --- Magic Methods (__dunder__) ---
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"
    def __len__(self):
        return self.pages
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

b1 = Book("Python 101", "John", 300)
b2 = Book("Python 101", "John", 300)
b3 = Book("Java 101", "Jane", 400)
print(b1)  # __str__
print(repr(b1))  # __repr__
print(f"len(b1)={len(b1)}")
print(f"b1==b2 {b1==b2}, b1==b3 {b1==b3}")
print(f"b1+b3 pages {b1+b3}")

# --- Inheritance vs Composition ---
# Inheritance: IS-A relation (Dog is Animal)
# Composition: HAS-A relation (Car has Engine) - Often better!

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # Composition: Car HAS engine
    def drive(self):
        return f"{self.brand} driving - {self.engine.start()}"

car = Car("Tata")
print(car.drive())

# --- Abstract Base Class (Interface) ---
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2*(self.w+self.h)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        import math
        return math.pi * self.r * self.r
    def perimeter(self):
        import math
        return 2 * math.pi * self.r

shapes = [Rectangle(4,5), Circle(7)]
for s in shapes:
    print(f"{s.__class__.__name__} area {s.area():.2f} peri {s.perimeter():.2f}")

# --- Property Decorator (Getter/Setter Pythonic) ---
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # _ means protected

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be 0-100")

    @property
    def grade(self):
        if self._marks >= 90:
            return "A"
        elif self._marks >= 75:
            return "B"
        elif self._marks >= 60:
            return "C"
        else:
            return "D"

s = Student("Amit", 85)
print(f"{s.name} marks {s.marks} grade {s.grade}")
s.marks = 95
print(f"After update marks {s.marks} grade {s.grade}")
# s.marks = 150  # Would raise ValueError

# --- EXERCISES ---
# 1. Create class Vector with x,y and implement __add__, __str__, __eq__ for vector addition
# 2. Create abstract class Animal with abstract method sound(), implement Dog, Cat
# 3. Use composition: Library has Books (Library class contains list of Book objects)
