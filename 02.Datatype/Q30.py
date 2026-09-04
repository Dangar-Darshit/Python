# Demonstrate differences (30)
values = [10, 10.0, "10", True, "True", None, "None"]

for v in values:
    print(repr(v), "->", type(v))
# Types printed beside each value show how they differ: int, float, str, bool, NoneType, etc.