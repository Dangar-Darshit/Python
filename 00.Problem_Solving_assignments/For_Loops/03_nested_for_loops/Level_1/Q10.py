n = int(input("Enter the number of rows you want: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2!=0:
            print("0", end=" ")
        elif j%2==0:
            print("1",end=" ")
    print()