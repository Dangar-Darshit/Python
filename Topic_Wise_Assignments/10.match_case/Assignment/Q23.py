atm = int(input("""Account Type:-
1 → Savings
2 → Current
type: """))

amt = int(input("Enter amount: "))
match atm:
    case 1:
        print("Saving Account")
        if amt > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
    case 2:
            print("Current Account")
            if amt > 0:
                print("Withdrawal Request Accepted")
            else:
                print("Invalid Amount")