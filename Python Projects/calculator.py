"""
Simple Calculator Program
This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide (x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

if __name__ == "__main__":
    print("Select Operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter Choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float (input("enter first number: "))
                num2 = float (input("enter second number: "))
            except ValueError:
                print("Invalid Input. Please enter a Number")
                continue
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        next_calculation = input("Let's do another calculation? (yes/no):")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")