word = input("Enter a word: ")
vowel = ""
consonant = ""


for i in word:
    for j in "AEIOUaeiou":
        is_vowel = False
        if (i==j):
            is_vowel = True
            break
        # elif (i!=j):
        #     consonant = "Consonant"
        # else:
        #     print(i, "= Consonant")


        if vowel == "Vowel":
            print(i, "= Vowel")
        else:
            print(i, "= Consonant")