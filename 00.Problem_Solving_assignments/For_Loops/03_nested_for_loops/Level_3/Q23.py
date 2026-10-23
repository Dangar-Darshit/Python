word = input("Enter a word: ")

for i in word:
    for j in word:
        if (i==j):
            print("Same")
        else:
            print("Different")