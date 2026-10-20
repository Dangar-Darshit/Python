num = input("Enter number squence with space: ").split()

for i in num:
    n = int(i)
    if n == 0:
        continue
    if n == -1:
        break
    print(n, end=" ")
else:
    print("\nAll values processed")