def stop_at_zero(n):
    if n == 0:
        return 0

    print(n)
    stop_at_zero(n-1)

stop_at_zero(5)