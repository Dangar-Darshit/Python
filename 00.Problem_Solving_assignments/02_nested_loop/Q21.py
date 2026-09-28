n = int(input("Enter a table number: "))
for j in range(1,11):
    for i in range(1,n+1):
        print(f"{i}x{j}={i*j}\t", end="\t")
    print()