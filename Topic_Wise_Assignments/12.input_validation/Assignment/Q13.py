n = int(input("Enter an integer between 0-100: "))

while n < 0 or n > 100:
    n = int(input("Enter an integer between 0-100 again: "))

print("Success")