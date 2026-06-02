def calculate(a, b, op):

    if op == "+":
        return a + b

    elif op == "-":
        return a - b

    elif op == "*":
        return a * b

    elif op == "/":
        return a / b

    else:
        return "Invalid Operator"


try:

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    op = input("Enter Operator (+,-,*,/): ")

    result = calculate(num1, num2, op)

    print(f"Result: {result}")

except ValueError:
    print("Invalid Number Entered")

except ZeroDivisionError:
    print("Cannot Divide By Zero")