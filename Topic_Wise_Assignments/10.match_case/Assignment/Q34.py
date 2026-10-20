game = int(input("""<---Travel Booking System--->
1 → Start Game
2 → Load Game
3 → Settings
4 → Exit
Enter choice: """))

match game :
    case 1:
        print("Starting Game...")
    case 2:
        print("Loading Game...")
    case 3:
        setting = int(input("Which Setting?:-\n1 → Sound\n2 → Graphics\n3 → Controls\nYour choice: "))
        match setting:
            case 1:
                print("Opening Sound Setting...")
            case 2:
                print("Opening Graphics Setting...")
            case 3:
                print("Oprning Controls Setting...")
    case 4:
        print("Exiting")
    case _:
        print("Invalid Choice")