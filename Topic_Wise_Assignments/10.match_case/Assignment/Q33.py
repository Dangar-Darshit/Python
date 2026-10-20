travel = int(input("""<---Travel Booking System--->
Travel With:-
1 → Flight
2 → Train
3 → Bus
Enter your choice: """))

match travel:
    case 1:
        flight = int(input("You want to travel:\n1 → Economy\n2 → Business\nYour choice: "))
        match flight:
            case 1:
                print("Opening Economy Section")
            case 2:
                print("Opening Business Section")
    case 2:
            train= int(input("You want to enter:\n1 → Sleeper\n2 → AC\nYour choice: "))
            match train:
                case 1:
                    print("Opening Sleeper Section")
                case 2:
                    print("Opening AC Section")
    case 3:
            bus = int(input("You want to see:\n1 → Ordinary\n2 → Volvo\nYour choice: "))
            match bus:
                case 1:
                    print("Opening Ordinary Section")
                case 2:
                    print("Opening Volvo Section")