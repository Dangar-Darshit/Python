exam = int(input("""Enter choice:
1 → Start Exam
2 → View Result
3 → Exit
Enter: """))

age = int(input("Enter your age: "))

match exam:
    case 1:
        if age >= 18:
            print("You can start the Exam")
        else:
            print("Invalid Age")
    case 2:
            if age >= 18:
                print("You can view result")
            else:
                print("Invalid Age")
    case 3:
          print("Exiting...")