light = input("Enter signal colour from below:-\n1. Red\n2. Yellow\n3.Green\nEnter Signal-> ").lower()
match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")