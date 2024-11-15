a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif operation == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif operation == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
elif operation == '/':
    # Check for division by zero
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid Operation...")
