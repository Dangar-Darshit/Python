main = int(input("""<---Main Menu--->
1 → Personal Banking
2 → Business Banking
Enter Banking Type: """))

match main:
    case 1:
        personal = int(input("""Select from below:-
        1 → Balance
2 → Transfer
3 → Loan
Enter Option: """))
        match personal:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Transfer Selected")
            case 3:
                print("Personal Loan Selected")
    case 2:
            business = int(input("""Select from below:-
            1 → Balance
2 → Payroll
3 → Business Loan
    Enter Option: """))
            match business:
                case 1:
                    print("Business Balance Selected")
                case 2:
                    print("Payroll Selected")
                case 3:
                    print("Business Loan Selected")
            