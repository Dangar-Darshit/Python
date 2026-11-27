s = input("Enter a string: ")
r = ""

for i in s:
    r = i + r

if s == r:
    print("YES")
else:
    print("NO")