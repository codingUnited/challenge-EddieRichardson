print("Welcome to your calculator!")

num1 = int(input("Enter the first number: "))
operator = input("Enter an operation (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

answer = eval(f"{num1} {operator} {num2}")

print("the answer is:", answer)
