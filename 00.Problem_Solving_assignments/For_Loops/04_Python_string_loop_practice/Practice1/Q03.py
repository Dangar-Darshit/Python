def pallindrome():
    str1 = input("Enter a word: ").lower()
    n = len(str1)
    flag1 = False
    flag2 = False


    for i in range(0,((n//2))):
        if str1[i]==str1[n//2]:
            flag1 = True

    for j in range((n//2),(n-1)):
        if str1[j]==str1[n-1]:
            flag2 = True

    if flag1 and flag2:
         print("yes")
    else:
         print("no")
   
pallindrome()