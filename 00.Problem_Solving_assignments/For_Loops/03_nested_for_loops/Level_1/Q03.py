char = input("Enter a character: ")
rows = int(input("Enter row number: "))
cols = int(input("Enter column number: "))

for row in range(rows):
    for col in range(cols):
        print(char, end=" ")
    print()