num = input("Enter number squence with space: ").split()
target = int(input("Enter your targeted number: "))
for i in num:
    n = int(i)
    if n < 0:
        continue
    if n == target:
        print("Target Found")
        break
else:
    print("Target Not Found")