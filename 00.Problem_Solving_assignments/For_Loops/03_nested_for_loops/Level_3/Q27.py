text = "BANANA".lower()
str1 = ""

for i in range(len(text)):
    char = text[i]

    # Skip if we have already counted this character
    if char in str1:
        continue

    count = 0
    for j in range(len(text)):
        if text[j] == char:
            count += 1

    print(f"{char} = {count}")
    str1 += char