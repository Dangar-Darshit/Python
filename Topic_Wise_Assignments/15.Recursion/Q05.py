def count(n):
    if n == 0:
        print("Done")
        return

    print(n, end=" ")
    count(n-1)

count(3)