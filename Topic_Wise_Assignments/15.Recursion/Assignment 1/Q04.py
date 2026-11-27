def answer(n):
    if n == 0:
        return 0

    return n + answer(n - 1)

print(answer(3))



# It gives TypeError because "int" + "NoneType" not possible 

# but if we write return just before recursive call then it works and prints 6