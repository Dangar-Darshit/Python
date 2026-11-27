s = input("Enter a string: ")
char = input("Enter a character that you have to remove: ")
r = ""

for i in s:
    if i == char:
        continue
    else:
        r += i

print(r)