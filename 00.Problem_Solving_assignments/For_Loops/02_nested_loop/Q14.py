n = int(input("Enter a number: "))
for i in range(2,n+1,2):
    for j in range(2,i+1,2):
        print(j, end=" ")
    print()