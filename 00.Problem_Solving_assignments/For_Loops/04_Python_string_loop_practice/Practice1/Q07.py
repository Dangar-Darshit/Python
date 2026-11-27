s = input("Enter a string: ").lower()
v = "aeiou"
count = 0

for i in s:
    if i in v:
        count += 1

print("Vowels: ", count)