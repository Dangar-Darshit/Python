s = input("Enter a string: ")
char = input("Which character yoiu want to count: ")
count = 0


for i in s:
    if i == char:
        count += 1


print(char, ":", count)