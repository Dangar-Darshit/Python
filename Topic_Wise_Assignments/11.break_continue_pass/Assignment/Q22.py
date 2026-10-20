num = input("Enter number squence with space: ").split()
target = int(input("Enter targeted no. : "))

for i in num:
    n = int(i)
    if n == target:
        print("Found")
        break
else:
    print("Not Found")