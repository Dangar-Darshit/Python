str1 = input("Enter a word: ")

for i in str1:
    if str1.count(i) == 2:
        print(i)
        break
else:
    print("No repeated character")