a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
cal = int(input("Enter symbol of operator:-\n1. +\n2. -\n3. *\n4. /\n Enter operator: "))
match cal:
    case 1:
        print("Addition", (a+b))
    case 2:
        print("Subtraction", (a-b))
    case 3:
        print("Multiplication", (a*b))
    case 4:
        print("Division", (a/b))