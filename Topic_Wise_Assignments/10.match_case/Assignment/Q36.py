pay = int(input("""<---Digital Payment Application--->
Payment Type:-
1 → UPI
2 → Card
3 → Wallet
Enter your choice: """))

match pay:
    case 1:
        upi = int(input("You want to Payment using:\n1 → Scan QR\n2 → Enter UPI ID\nYour choice: "))
        match upi:
            case 1:
                print("Opening Scan QR")
            case 2:
                print("Opening Enter UPI ID")
    case 2:
            card = int(input("You want to Payment using:\n1 → Credit Card\n2 → Debit Card\nYour choice: "))
            match card:
                case 1:
                    print("Opening Credit Card Section")
                case 2:
                    print("Opening Debit Card Section")
    case 3:
            wallet = int(input("You want to :\n1 → Add Money\n2 → Pay Using Wallet\nYour choice: "))
            match wallet:
                case 1:
                    print("Opening Add Money Section")
                case 2:
                    print("Opening Pay Using Wallet Section")