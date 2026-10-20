def calculate(a, b, c):
    if (a<b) and (a<c):
        small = a
    elif (b<a) and (b<c):
        small = b
    elif (c<a) and (c<b):
        small = c

    if (a>b) and (a>c):
        large = a
    elif (b>a) and (b>c):
        large = b
    elif (c>b) and (c>a):
        large = c

    sum = a + b + c
    return small, large, sum

s, l, t = calculate(12, 33, 63)

print(f"Smallest:{s}\nLargest:{l}\nTotal:{t}")