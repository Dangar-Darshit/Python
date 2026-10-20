
str1 = input("Enter a word: ").lower()
rstr = ""
i = len(str1) - 1
while i >= 0:
    rstr = rstr + str1[i]
    i = i - 1
if str1 == rstr:
    print("String is pallindrome")
else:
    print("String is not pallindrome")

str1 = input("Enter a word: ").lower()
rstr = ""
i = -1
while i >= -len(str1):
    rstr = rstr + str1[i]
    i = i - 1
if str1 == rstr:
    print("String is pallindrome")
else:
    print("String is not pallindrome")



str1 = input("Enter a word: ").lower()
i = -len(str1)
j = -1
flag = True
while (i < j and flag):
    if str1[i] == str1[j]:
        flag = True
        i = i + 1
        j = j - 1
    else:
        flag = False
        # i = j

if flag == True:
    print("String is pallindrome")
else:
    print("String is not pallindrome")