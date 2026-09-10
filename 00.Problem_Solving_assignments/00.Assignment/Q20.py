a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")
