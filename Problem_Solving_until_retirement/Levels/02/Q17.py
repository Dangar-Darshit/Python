n = int(input("Enter a number: "))
for i in range(1,11):
    for j in range(1,(n+1)):
        print(f"{j} x {i} = {i*j}", end="\t")
    print()