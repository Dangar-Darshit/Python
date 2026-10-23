n = int(input("Enter the number of row: "))
c = int(input("Enter column number: "))
for i in range(1,n+1):
    for j in range(1,c+1):
        if j%2==0:
            print(j, end=" ")
    print()