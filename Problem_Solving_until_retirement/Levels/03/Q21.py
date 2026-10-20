digit = 0
num = input("Enter a number: ")
for i in num:
    if i.isdigit():
        digit += 1

print(digit)