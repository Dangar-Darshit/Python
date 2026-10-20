bank = int(input("""<---Banking Service-->
1 → Account Balance
2 → Mini Statement
3 → Fund Transfer
4 → Bill Payment
5 → Customer Support
Enter Service : """))


match bank:
    case 1:
        print("Opening Account Balance")
    case 2:
        print("Opening Mini Statement")
    case 3:
        print("Opening Fund Transfer")
    case 4:
        print("Opening Bill Payment")
    case 5:
        print("Opening Customer Support")
    case _:
        print("Invalid Choice")