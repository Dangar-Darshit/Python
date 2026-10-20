num = input("Enter number squence with space: ").split()

for i in num:
    n = int(i)
    if n < 0:
        break
    print(n, end=" ")