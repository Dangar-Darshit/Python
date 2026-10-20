while True:
    password = input("Enter a password: ")
    valid = True

    if len(password) < 8:
        print("At least 8 characters")
        valid = False

    up = low = dig = False
    for c in password:
        if c.isupper():
            up = True
        if c.islower():
            low = True
        if c.isdigit():
            dig = True

    if not up:
        print("At least one uppercase letter")
        valid = False
    if not low:
        print("At least one lowercase letter")
        valid = False
    if not dig:
        print("At least one digit")
        valid = False

    for c in password:
        if c.isspace():
            print("No whitespace characters")
            valid = False
            break

    if valid:
        print("Password accepted.")
        break