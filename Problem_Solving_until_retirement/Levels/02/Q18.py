count = 0
n = int(input("Enter a number: "))
for i in range(1,(n+1)):
    if i % 3 == 0:
        count += 1
print(count)