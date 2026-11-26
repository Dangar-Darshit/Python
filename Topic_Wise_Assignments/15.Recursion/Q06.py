def count_up(n):
    if n == 0:
        return

    count_up(n-1)
    print(n)


count_up(4)