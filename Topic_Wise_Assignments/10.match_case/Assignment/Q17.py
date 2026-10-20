acc = int(input("Enter Account Type:-\n1. Savings\n2. Current\n:- "))

match acc:
    case 1:
        print("Savings Account")
        check = int(input("Select one:-\n1 → Check Balance\n2 → Deposit\n3 → Withdraw\nYou Selected: "))
        match check:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
    case 2:
            print("Current Account")
            check = int(input("Select one:-\n1 → Check Balance\n2 → Deposit\n3 → Withdraw\nYou Selected: "))
            match check:
                case 1:
                    print("Check Balance Selected")
                case 2:
                    print("Deposit Selected")
                case 3:
                    print("Withdraw Selected")
            