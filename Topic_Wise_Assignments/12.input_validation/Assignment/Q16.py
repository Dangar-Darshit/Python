a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
opr = input("Enter operations sign:\n(+)-Addition\n(-)-Subtrastion\n(*)-Multiplication\n(/)-Division\nYour Operation: ")

while True:
    match opr:
        case "+":
            print(a+b)
        case "-":
            print(abs(a-b))
        case "*":
            print(a*b)
        case "/":
            print(a/b)
        case _:
            print("Invalid Choice!!!")
            opr = input("Enter operations valid sign:\n(+)-Addition\n(-)-Subtrastion\n(*)-Multiplication\n(/)-Division\nYour Operation: ")