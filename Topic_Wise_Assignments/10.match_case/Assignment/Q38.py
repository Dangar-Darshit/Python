main = int(input("""<---Smart Vehicle Dashboard--->
Select from below:-
1 → Engine
2 → Lights
3 → Music
4 → Navigation
Enter: """))

match main:
    case 1:
        engine = int(input("Select:\n1 → Start\n2 → Stop\nYour choice: "))
        match engine:
            case 1:
                print("Starting Engine")
            case 2:
                print("Stopping Engine")
    case 2:
            lights = int(input("Select:\n1 → Headlights\n2 → Indicators\n3 → Hazard Lights\nYour choice: "))
            match main:
                case 1:
                    print("Start Headlights")
                case 2:
                    print("Start Indicators")
                case 3:
                    print("Start Hazard Lights")
    case 3:
            music = int(input("Select:\n1 → Play\n2 → Pause\n3 → Next\n4 → Previous\nYour choice: "))
            match music:
                case 1:
                    print("Play Music")
                case 2:
                    print("Pause Music")
                case 3:
                    print("Next")
                case 4:
                    print("Previous")
    case 4:
                nav = int(input("Select:\n1 → Start Navigation\n2 → Stop Navigation\nYour choice: "))
                match nav:
                    case 1:
                        print("Start Navigation")
                    case 2:
                        print("Stop Navigation")