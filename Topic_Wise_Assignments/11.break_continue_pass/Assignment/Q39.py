num = input("Enter a number list with space: ").split()

for i in num:
    n = int(i)
    if n < 0:
        continue
    if n%4==0 and n%6==0:
        print(f"Found: {n}")
        break
else:
    print("No matching number")