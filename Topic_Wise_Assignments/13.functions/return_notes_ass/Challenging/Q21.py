def analyze_number(number):
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number

    is_even = (number % 2 == 0)
    digit_count = len(str(absolute_value))

    return absolute_value, is_even, digit_count

print(analyze_number(-1234))
print(analyze_number(7))
print(analyze_number(0))