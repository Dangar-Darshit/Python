n = int(input("Enter your selected dish number from below:-\n1. Pizza\n2. Burger\n3. Pasta\n4. Sandwich\nYour dish no.-> "))
match n:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")
    case 4:
        print("You selected Sandwich")
    case _:
        print("Invalid Menu choice")