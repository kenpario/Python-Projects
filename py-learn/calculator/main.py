import math

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /, %, **): ")
if operation == "+":
    result = round(x + y,2)
elif operation == "-":
    result = round(x - y,2)
elif operation == "*":
    result = round(x * y,2)
elif operation == "/":
    result = round(x / y,2)
elif operation == "%":
    result = round(x % y,2)
elif operation == "**":
    result = round(x ** y,2)
else:
    print(f"Invalid operation: {operation}")
    result = None

print(f"The result is: {result}")