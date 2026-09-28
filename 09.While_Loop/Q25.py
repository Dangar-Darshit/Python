string = input("Enter a word: ")
i = 0
count = 0

while i < len(string):
    if "A" <= string[i] <= "Z":
        count += 1
    i += 1

print(count)