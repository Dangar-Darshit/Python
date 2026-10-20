str1 = input("Enter any string: ").lower()
remove = input("Enter a character you don't want to display: ").lower()
for i in str1:
    if i == remove:
        continue
    print(i, end="")