def total(n):
    if n == 0:          #Base Case
        return 0

    return n + total(n - 1)


# It stops recursion because in base case there is condition which gets true and returns any value(here 0) and the further code doesnt runs.