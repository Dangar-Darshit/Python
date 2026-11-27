def even_sum(n):
    if n == 0:
        return 0

    digit = (n // 10) % 10

    if n >= 10:
        return digit + even_sum(n // 100)
    else:
        return 0

print(even_sum(583246))