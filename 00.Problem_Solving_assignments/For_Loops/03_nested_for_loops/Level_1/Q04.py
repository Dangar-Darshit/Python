rows = int(input("Enter row number: "))
cols = int(input("Enter column number: "))

for row in range(rows):
    for col in range(cols):
        print(f"({row},{col})", end=" ")
    print()