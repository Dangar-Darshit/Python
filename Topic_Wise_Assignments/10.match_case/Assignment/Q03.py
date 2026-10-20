atm = int(input("Enter number you want to select from below:-\n1 → Check Balance\n2 → Withdraw Money\n3 → Deposit Money\n4 → Change PIN\n5 → Exit\n Your choice -> "))
match atm:
    case 1:
        print("Check Balance Selected")
    case 2:
        print("Withdraw Money Selected")
    case 3:
        print("Deposit Money Selected")
    case 4:
        print("Change PIN Selected")
    case 5:
        print("Exiting...")
    case _:
        print("Invalid No. Selected")