def count(n):
    if n == 0:
        return

    count(n + 1)

print(count(2))
# It does not reach to the base case because when the recusive call is happend the argument is is getting incremented so it does not reach to 0 at any cost.(it shows RecursionError)