def mystery(n):
    if n <= 1:
        return n

    return mystery(n - 1) + mystery(n - 2)

print(mystery(4))  # 3
print(mystery(0))  # 0 
print(mystery(1))  # 1
print(mystery(2))  # 1