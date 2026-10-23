n = int(input("Enyer number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==j):
            print("Same", end=" ")
        else:
            print("Different", end=" ")
    print()