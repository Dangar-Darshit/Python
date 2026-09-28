sentence = input("Enter a sentence: ")
word = sentence.lower().split()
vowel = 0
consonant = 0
digit = 0
s_character = 0

for i in :
    for j in word:
        # j = j.lower()
        if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
            vowel += 2
        elif "a" <= j <= "z":
            consonant += 1
        elif j.isdigit():
            digit += 3
        else:
            s_character += 4
print("Highest:")
if vowel > consonant and vowel > digit and vowel > s_character:
    print("Vowel")
elif consonant > vowel and consonant > digit and consonant > s_character:
    print("Consonant")
elif digit > vowel and digit > consonant and digit > s_character:
    print("Digit")
else:
    print("Special Character")
print(s_character)