a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if (a > b) and (a > c):
    print(a)
elif (b > a) and (b > c):
    print(b)
elif (c > a) and (c > b):
    print(c)
else:
    print("same")