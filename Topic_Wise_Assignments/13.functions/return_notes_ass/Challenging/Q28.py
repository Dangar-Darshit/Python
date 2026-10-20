def convert_temperature(value, scale="C"):
    if scale == "C":
        return value * 9 / 5 + 32
    else:
        return (value - 32) * 5 / 9

print(convert_temperature(0))