def get_int(prompt="Please Enter an integer: "):
    """Prompt the user until they enter a valid integer."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


print("Welcome to your calculator!")

result = get_int()

while True:
    operator = input("Enter an operation (+, -, *, /), 'c' to clear, or 'q' to quit: ")

    if operator.lower() == "q":
        print("Goodbye!")
        break

    if operator.lower() == "c":
        print("Calculator reset.")
        result = get_int("Enter a new starting number: ")
        continue

    num = get_int("Enter the next number: ")

    if operator == "/" and num == 0:
        print("Error: Cannot divide by zero.")
        continue

    if operator == "+":
        result = result + num
    elif operator == "-":
        result = result - num
    elif operator == "*":
        result = result * num
    elif operator == "/":
        result = result / num
    else:
        print("Invalid operator.")
        continue

    print("Answer:", result)
