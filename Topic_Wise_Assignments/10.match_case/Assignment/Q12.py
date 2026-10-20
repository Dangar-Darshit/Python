user = input("""<---User Role--->
admin
teacher
student
guest
Your Are: """)

match user:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest":
        print("Limited Access")
    case _:
        print("Invalid User")