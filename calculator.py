def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Surely! You cannot divide by zero!")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in operations:
            return operations[op]
        else:
            print("Please enter one of +, -, *, /.")

def calculator():
    print("By your best developer: Ian Mutugi Kinyua")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    try:
        result = operation(num1, num2)
        print(f"The result is: {result}")
        print("run 'python calculator.py' to perform another calculation")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
