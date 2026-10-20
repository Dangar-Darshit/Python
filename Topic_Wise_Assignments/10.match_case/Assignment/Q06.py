menu = int(input("""<--Online Shopping Menu-->
1 → Electronics
2 → Clothing
3 → Books
4 → Grocery
5 → Exit
Your Choice -> """))

match menu:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case 5:
        print("Exiting...")
    case _:
        print("Invalid Choice")