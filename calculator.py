import math
from sys import exception

def calculator():
    print("Standard Calculator")
    try:
        while True:
            op = input("Enter operation (+, -, *, /, sin, cos, tan, sqrt, exit): ").lower()
            if op == "exit":
                print("Exiting the calculator")
                break

            list_op = ["+", "-", "/", "*", "sin", "cos", "tan", "sqrt"]
            if op not in list_op:
                print("Please enter a valid operator")
                continue

            # Handle trigonometric and sqrt functions (single number operations)
            if op in ["sin", "cos", "tan", "sqrt"]:
                while True:
                    number = input("Enter number (or 'back' to choose another operation): ")
                    if number.lower() == "back":
                        break
                    try:
                        num = float(number)
                        if op == "sin":
                            result = math.sin(math.radians(num))  # using degrees for input
                            print(f"sin({num}) = {result}")
                        elif op == "cos":
                            result = math.cos(math.radians(num))  # using degrees for input
                            print(f"cos({num}) = {result}")
                        elif op == "tan":
                            result = math.tan(math.radians(num))  # using degrees for input
                            print(f"tan({num}) = {result}")
                        elif op == "sqrt":
                            if num < 0:
                                print("Cannot calculate square root of a negative number")
                                continue
                            result = math.sqrt(num)
                            print(f"√{num} = {result}")
                        break
                    except ValueError:
                        print("Please enter a valid number!")
                continue

            # Handle basic arithmetic operations (multiple numbers)
            numbers = []
            while True:
                number = input("Enter number or = sign to calculate: ")
                if number == "=":
                    if len(numbers) < 2:
                        print("Enter at least 2 numbers")
                        continue
                    break
                try:
                    num = float(number)
                    numbers.append(num)
                except ValueError:
                    print("Enter numbers only!")
                    continue

            if op == "+":
                result = numbers[0]
                for number in numbers[1:]:
                    result += number
                print(" + ".join(map(str, numbers)) + " = " + f"{result}")

            elif op == "-":
                result = numbers[0]
                for number in numbers[1:]:
                    result -= number
                print(" - ".join(map(str, numbers)) + " = " + f"{result}")

            elif op == "*":
                result = numbers[0]
                for number in numbers[1:]:
                    result *= number
                print(" * ".join(map(str, numbers)) + " = " + f"{result}")

            elif op == "/":
                result = numbers[0]
                try:
                    for number in numbers[1:]:
                        result /= number
                    print(" / ".join(map(str, numbers)) + " = " + f"{result}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed")

    except Exception as e:
        print(f"Invalid operation: {e}")
    print("Developed by: haymanot")


