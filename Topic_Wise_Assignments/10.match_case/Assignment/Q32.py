user = int(input("""<---School Management System--->
Login With:-
1 → Student
2 → Teacher
3 → Parent
User Role: """))

match user:
    case 1:
        student = int(input("You want to see:\n1 → Marks\n2 → Attendence\n3 → Homework\nYour choice: "))
        match student:
            case 1:
                print("Opening Marks")
            case 2:
                print("Opening Attendence")
            case 3:
                print("Opening Homework")
    case 2:
            teacher = int(input("You want to enter:\n1 → Enter Marks\n2 → Attendence\n3 → Assign Homework\nYour choice: "))
            match teacher:
                case 1:
                    print("Opening Enter Marks")
                case 2:
                    print("Opening Attendence")
                case 3:
                    print("Opening Assign Homework")
    case 3:
            parent = int(input("You want to see:\n1 → Child Marks\n2 → Child Attendence\n3 → Contact Teacher\nYour choice: "))
            match parent:
                case 1:
                    print("Opening Child Marks")
                case 2:
                    print("Opening Child Attendence")
                case 3:
                    print("Opening Contact Teacher")