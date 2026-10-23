n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==j):
            print("SPECIAL", end="\t")
        elif (i+j)==n:
            print("PAIR", end="\t")
        else:
            print("NORMAL", end="\t")
    print()