text = input("Enter: ")
target = input("Enter your targeted string or number: ")
found = False

for i in range(len(text) - len(target) + 1):
    if text[i:(i + len(target))] == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")