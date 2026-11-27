s = input("Enter a string: ")
char = input("Enter a character that you have to find index: ")

for i in range(len(s)):
    if s[i] == char:
        print(i)
        break
else:
    print(-1)