portal = int(input("""<---University Portal--->
1 → Student
2 → Teacher
You Are : """))

match portal:
    case 1:
        s = int(input("Select from below\n1 → View Courses\n2 → View Marks\n3 → View Attendance\nEnter Your choice : "))
        match s:
            case 1:
                print("Opening Student Couses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendence")
    case 2:
        t = int(input("Select from below\n1. View Students\n2. Enter Marks\n3. View Attendence\nEnter Your Choice : "))
        match t:
            case 1:
                print("Opening Student List")
            case 2:
                print("Opening Enter Marks Page")
            case 3:
                print("Opening Attendence")