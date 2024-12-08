def calculator():
    print("Simple Python Calculator")
    print("Available Operations: +, -, *, /")
    print("Type 'exit' anytime to quit.\n")

    while True:
        num1 = input("Enter the first number (or 'exit'): ")
        if num1.lower() == 'exit':
            print("Exiting... Goodbye!")
            break

        operator = input("Enter an operation (+, -, *, /): ")
        num2 = input("Enter the second number: ")

        # Validate input
        if not num1.isdigit() or not num2.isdigit():
            print("Invalid input. Please enter numbers only.\n")
            continue

        num1 = float(num1)
        num2 = float(num2)

        # Perform calculations
        if operator == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}\n")
        elif operator == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}\n")
        elif operator == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}\n")
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.\n")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}\n")
        else:
            print("Invalid operation. Please use +, -, *, or /.\n")

calculator()
