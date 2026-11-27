# Do not use max(), loops, or convert the number to a string.
def max_digit(n):
    if n < 10:
        return n

    last_digit = n % 10
    remaining_number = max_digit(n // 10)

    if last_digit > remaining_number:
        return last_digit
    return remaining_number

print(max_digit(4729))  # 9
print(max_digit(555))   # 5
print(max_digit(0))     # 0