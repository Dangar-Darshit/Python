number = int(input("Enter a number: "))
if number%5 == 0 and number%11 == 0:
    print(f"{number} is divisible by both 5 and 11")
elif number%5 == 0:
    print(f"{number} is only divisible by 5")
elif number%11 == 0:
    print(f"{number} is only divisible by 11")
elif number%5 != 0 and number%11 != 0:
    print(f"Divisible by neither")