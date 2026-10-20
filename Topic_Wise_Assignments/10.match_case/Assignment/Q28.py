ticket = int(input("""<----Railway Ticket System---->
1 → Book Ticket
2 → Cancel Ticket
3 → Check PNR
4 → Train Schedule
5 → Exit
Enter your aaction: """))

match ticket:
    case 1:
        print("Book Ticket Selected")
    case 2:
        print("Cancel Ticket Selected")
    case 3:
        print("Check PNR Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exiting")
    case _:
        print("Invalid Selection")