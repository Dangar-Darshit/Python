role = int(input("""
Main Menu
1 -> Employee
2 -> Manager
Enter role: """))

match role:
    case 1:  # Employee
        option = int(input("""
Employee
1 -> View Profile
2 -> Apply Leave
3 -> View Salary
Enter option: """))
        match option:
            case 1:
                print("Viewing Profile")
            case 2:
                days = int(input("Enter number of leave days: "))
                if days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("Viewing Salary")
            case _:
                print("Invalid Employee option")

    case 2:  # Manager
        option = int(input("""
Manager
1 -> View Team
2 -> Approve Leave
3 -> View Reports
Enter option: """))
        match option:
            case 1:
                print("Viewing Team")
            case 2:
                print("Approving Leave")
            case 3:
                print("Viewing Reports")
            case _:
                print("Invalid Manager option")

    case _:
        print("Invalid role")