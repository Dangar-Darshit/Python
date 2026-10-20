str1 = input("Enter a sentence: ").lower()
str2 = str1.split()
target = input("Which word you want to find : ").lower()
for i in str2:
    if i == target:
        print("Found")
        break
else:
    print("Not Found")