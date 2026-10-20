choice = int(input("""<-------------Student Portal Menu-------------->
1. View Profile
2. View Courses
3. View Marks
4. View Attendance
5. Logout
Your choice -> """))

match choice:
    case 1:
        print("Opening Profile")
    case 2:
        print("Opening Cources")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendence")
    case 5:
        print("Logging Out...")
    case _:
        print("Invalid Choice")