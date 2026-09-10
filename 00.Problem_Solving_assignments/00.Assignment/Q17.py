a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a / b)
else:
    print("Invalid operator")
