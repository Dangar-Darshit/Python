for i in range(5):
    num = int(input("Enter number: "))
    text = str(num)
    even = 0
    odd = 0

    for j in text:
        n = int(j)
        if n % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

    if even > odd:
        print("Even more")
    elif odd > even:
        print("Odd more")
    else:
        print("Equal")