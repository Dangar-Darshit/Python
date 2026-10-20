str1 = input("Enter a string: ")
target = input("Enter a character you want to target: ")

for i in str1:
    if i == target:
        print("Character exists")
        break  
else:
    print("Character missing")