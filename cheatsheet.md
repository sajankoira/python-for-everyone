# Python Complete Cheatsheet 📚 (Full Version)

## Basics
```python
print("Hello")          # output
name = input("Name: ")  # input always str
# comment
x = 10      # int
y = 3.14    # float
s = "Hi"    # str
b = True    # bool
print(f"{x} + {y}")     # f-string best!
```

## Operators
```
+ - * / // % **        # arithmetic, // floor, % mod, ** power
== != > < >= <=        # comparison
and or not             # logical
in not in              # membership
is is not              # identity
+= -= *= /=            # assignment shorthand
```

## If-Else
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# Ternary
status = "Adult" if age>=18 else "Minor"
```

## Loops
```python
for i in range(5):       # 0-4
for i in range(1,6):     # 1-5
for i in range(0,10,2):  # step 2
for char in "Python":    # iterate string/list
    print(char)

count=0
while count<5:
    print(count)
    count+=1

break      # exit loop
continue   # skip current
```

## Strings
```python
s="Python"
s[0], s[-1], s[0:4], s[::-1]   # indexing slicing reverse
len(s), s.upper(), s.lower(), s.strip(), s.replace("P","J")
s.split(), " ".join(list), s.count("y"), s.find("th")
```

## Lists (Mutable)
```python
lst=[1,2,3]
lst[0], lst[-1], lst[1:3]
lst.append(4), lst.insert(0,0), lst.remove(2), lst.pop(), lst.sort(), lst.reverse()
[lst for lst in ...]  # comprehension
squares=[x*x for x in range(10) if x%2==0]
```

## Tuples (Immutable)
```python
t=(1,2,3)
x,y= (10,20)  # unpack
a,b=b,a       # swap
```

## Dict (key:value)
```python
d={"name":"Amit","age":21}
d["name"], d.get("grade","NA"), d["grade"]="A"
d.keys(), d.values(), d.items()
for k,v in d.items(): print(k,v)
{x:x*x for x in range(5)}  # dict comprehension
```

## Set (Unique)
```python
s={1,2,3}, s=set(), s.add(4)
A|B union, A&B intersection, A-B diff, A^B sym diff
```

## Functions
```python
def add(a,b=0):
    """docstring"""
    return a+b

add(2,3), add(a=2,b=3)

*args = tuple of args
**kwargs = dict of kwargs

lambda x: x*x
map(lambda x:x*x, [1,2,3]) -> [1,4,9]
filter(lambda x:x%2==0, [1,2,3,4]) -> [2,4]
```

## OOP
```python
class Dog:
    species="Canis"  # class attr
    def __init__(self,name,age):  # constructor
        self.name=name
    def bark(self):
        return f"{self.name} Woof!"
    def __str__(self):
        return self.name

dog=Dog("Bruno",3)
dog.bark()

# Inheritance
class Puppy(Dog):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed

# Encapsulation
self._protected, self.__private, @property
```

## File Handling
```python
with open("file.txt","w") as f:
    f.write("Hi\n")

with open("file.txt","r") as f:
    content=f.read()          # full
    lines=f.readlines()       # list
    for line in f: print(line)

import json
json.dump(obj, open("data.json","w"), indent=4)
data=json.load(open("data.json"))

import csv
with open("a.csv","w",newline="") as f:
    csv.writer(f).writerows([["a","b"],[1,2]])
```

## Exception
```python
try:
    x=int(input())
    10/x
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Divide by zero")
except Exception as e:
    print(e)
else:
    print("No error")
finally:
    print("Always")

raise ValueError("Custom error")

class MyError(Exception): pass
```

## Modules
```python
import math, random, datetime
from math import pi
import numpy as np   # alias
# pip install requests
# python -m venv venv
```

## Advanced
```python
# Generator
def gen(n):
    for i in range(n):
        yield i
g=gen(5)
list(g)

# Decorator
def deco(func):
    def wrapper(*a,**k):
        print("Before")
        r=func(*a,**k)
        print("After")
        return r
    return wrapper
@deco
def hello(): print("Hi")

# Iterator
it=iter([1,2,3])
next(it)
```

## Interview Quick
- List vs Tuple: List mutable, Tuple immutable + faster + key in dict
- == vs is: == checks value, is checks memory identity
- Deep copy: import copy; copy.deepcopy(list)
- LEGB: Local Enclosing Global Built-in scope rule
- GIL: Global Interpreter Lock - Python threads not truly parallel
- PEP8: snake_case, 4 spaces, 79 chars

Full repo: github.com/sajankoira/python-for-everyone
