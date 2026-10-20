str1 = input("Enter any string: ")
target = input("What you want to find: ")
for i in str1:
    print(i, end=" ")
    if i == target:
        break