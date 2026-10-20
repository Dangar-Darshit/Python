valid = False

while not valid:
    num = int(input("Enter an integer from 1 to 10: "))
    if 1 <= num <= 10:
        valid = True
    else:
        print("Invalid value. Please try again.")

print("You entered:", num)