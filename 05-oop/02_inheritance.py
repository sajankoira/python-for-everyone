"""
TOPIC: OOP - Inheritance, Encapsulation, Polymorphism
"""

# --- Inheritance: Child gets properties of Parent ---

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Override parent method (Polymorphism)
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    # If no speak override, will use parent's speak
    pass

dog = Dog("Bruno")
cat = Cat("Whiskers")
cow = Cow("Gauri")

print(dog.eat())  # Inherited from Animal
print(dog.speak())  # Overridden
print(cat.speak())
print(cow.speak())  # Uses parent

# Types of Inheritance

# Multiple Inheritance
class Flyer:
    def fly(self):
        return "Flying!"

class Swimmer:
    def swim(self):
        return "Swimming!"

class Duck(Animal, Flyer, Swimmer):  # Inherits from 3!
    def speak(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(f"\n{duck.eat()}, {duck.fly()}, {duck.swim()}, {duck.speak()}")

# --- Encapsulation: Public, Protected, Private ---

class BankAccount:
    def __init__(self, balance):
        self.public = "Everyone can see me"
        self._protected = "Should not access directly, but can"  # Convention with _
        self.__private = balance  # Name mangling - truly private with __

    def get_private(self):  # Getter
        return self.__private

    def set_private(self, val):  # Setter with validation
        if val >= 0:
            self.__private = val

acc = BankAccount(1000)
print(f"\nPublic: {acc.public}")
print(f"Protected: {acc._protected}")
# print(acc.__private)  # Error! AttributeError
print(f"Private via getter: {acc.get_private()}")
print(f"Private via name mangling (hack): {acc._BankAccount__private}")  # Not recommended!

# --- Polymorphism Example ---
def animal_sound(animal):  # Works with any Animal type
    print(animal.speak())

print("\n--- Polymorphism in action ---")
for a in [dog, cat, cow, duck]:
    animal_sound(a)

# --- super() - Call Parent Constructor ---
class Puppy(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call Dog.__init__
        self.breed = breed
    
    def bark(self):  # Override but also use parent
        return super().bark() + " ... in puppy voice!"

puppy = Puppy("Tommy", 1, "Labrador")
print(f"\nPuppy: {puppy.name}, {puppy.breed}, {puppy.bark()}")

# --- EXERCISES ---
# 1. Create parent class Vehicle with start(), stop(). Child classes Car, Bike override.
# 2. Create class Employee with name, salary. Manager inherits and adds bonus. Override to show total salary
# 3. Create encapsulation example: Student with private __marks, getter, setter that ensures 0-100
