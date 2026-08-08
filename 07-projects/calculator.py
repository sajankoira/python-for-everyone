"""
PROJECT 1: Simple Calculator
Concepts: Functions, Loops, If-Else, Exception Handling
"""

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b==0:
        return "Error: Division by zero!"
    return a/b
def power(a,b): return a**b

def calculator():
    print("=== Simple Calculator ===")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power")
    
    while True:
        choice = input("\nEnter choice (1-5 or q to quit): ").strip()
        if choice.lower() == 'q':
            print("Bye!")
            break
        
        if choice not in ['1','2','3','4','5']:
            print("Invalid choice!")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1,num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {sub(num1,num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {mul(num1,num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {div(num1,num2)}")
        elif choice == '5':
            print(f"Result: {num1} ** {num2} = {power(num1,num2)}")

if __name__ == "__main__":
    # Only run if this file is executed directly
    calculator()
