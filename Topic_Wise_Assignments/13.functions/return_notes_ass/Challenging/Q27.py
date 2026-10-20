def compare(a, b):
    if a>b:
        l = "A is greater"
    elif b>a:
        l = "B is greater"
    else:
        l = "Both are Equal"

    diff = a-b
    if diff <0:
        diff = -diff

    return l, diff

greater , sub = compare(-56,-44)
print(greater)
print(sub)