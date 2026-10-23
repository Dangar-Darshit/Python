string = input("Enter a string: ")
upper = 0
lower = 0
digit = 0
space = 0
s_character = 0
for i in string:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        s_character += 1

if string!="":
    if upper > lower and upper > digit and upper > space and upper > s_character:
        print(f"Highest: {upper} Upper")
    elif lower > upper and lower > digit and lower > space and lower > s_character:
        print(f"Highest: {lower} Lower")
    elif digit > lower and upper < digit and digit > space and digit > s_character:
        print(f"Highest: {digit} Digit")
    elif space > lower and space > digit and upper < space and space > s_character:
        print(f"Highest: {space} Space")
    elif s_character > lower and s_character > digit and upper < s_character and space < s_character:
        print(f"Highest: {s_character} Special Character")
    elif upper == lower or upper == digit or upper == space or upper == s_character:
        print("Tie")
    elif lower == upper or lower == digit or lower == space or lower == s_character:
        print("Tie")
    elif digit == lower or upper == digit or digit == space or digit == s_character:
        print("Tie")
    elif space == lower or space == digit or upper == space or space == s_character:
        print("Tie")
    else:
        print("Tie")