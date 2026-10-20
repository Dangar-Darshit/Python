n = int(input("Enter a number: "))

while n%3!=0 and n%5!=0:
    n = int(input("Enter a number again: "))

print("Accepted number:", n)