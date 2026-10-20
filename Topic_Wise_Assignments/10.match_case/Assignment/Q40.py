role = int(input("""
Main Menu
1 -> Student
2 -> Teacher
3 -> Administration
Enter role: """))

match role:
    case 1:
        option = int(input("""
Student
1 -> Profile
2 -> Marks
3 -> Attendance
4 -> Courses
Enter option: """))
        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Student option")

    case 2:
        option = int(input("""
Teacher
1 -> Students
2 -> Enter Marks
3 -> Attendance
4 -> Courses
Enter option: """))
        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Teacher option")

    case 3:
        option = int(input("""
Administration
1 -> Fees
2 -> Admissions
3 -> Notices
4 -> Departments
Enter option: """))
        match option:
            case 1:
                print("Opening Administration Fees")
            case 2:
                print("Opening Administration Admissions")
            case 3:
                print("Opening Administration Notices")
            case 4:
                print("Opening Administration Departments")
            case _:
                print("Invalid Administration option")

    case _:
        print("Invalid role")