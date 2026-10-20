str1 = input("Enter any string: ").lower()
count = 0
vowels = "aeiou"
for i in str1:
    if i in vowels:
        continue
    count += 1
print(count)