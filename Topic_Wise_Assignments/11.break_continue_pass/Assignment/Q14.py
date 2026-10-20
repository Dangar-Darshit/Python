num = input("Enter marks squence with space: ").split()

for i in num:
    n = int(i)
    if n < 40:
        continue
    print(n, end=" ")