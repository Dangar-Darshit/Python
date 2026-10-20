learn = int(input("""<---Online Learning Platform--->
Select language:-
1 → Programming
2 → Mathematics
3 → Communication
learn: """))

match learn:
    case 1:
        programming = int(input("You want to learn:\n1 → Python\n2 → Java\n3 → C++\nYour choice: "))
        match programming:
            case 1:
                print("Selected Python")
            case 2:
                print("Selected Java")
            case 3:
                print("Selected C++")
    case 2:
            maths = int(input("You want to learn:\n1 → Algebra\n2 → Calculus\n3 → Statistics\nYour choice: "))
            match maths:
                case 1:
                    print("Selected Algebra")
                case 2:
                    print("Selected Calculus")
                case 3:
                    print("Selected Statistics")
    case 3:
            communication = int(input("You want to learn:\n1 → English\n2 → Presentation\n3 → Interview Skills\nYour choice: "))
            match communication:
                case 1:
                    print("Selected English")
                case 2:
                    print("Selected Presentation")
                case 3:
                    print("Selected Interview Skills")