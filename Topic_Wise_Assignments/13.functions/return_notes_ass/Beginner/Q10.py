def get_min_max(a,b):
    if a<b:
        return a, b
    return b, a

min, max = get_min_max(20,50)

print("Min.", min,"Max.", max)