movie = int(input("""Select from below:-
1 → Regular
2 → Premium
3 → VIP
Enter seat category no.: """))

age = int(input("Enter age : "))

match movie:
    case 1:
        if age <= 5:
            print("Free Entry")
        else:
            print("Regular Seat Selected")
    case 2:
            if age <= 5:
                print("Free Entry")
            else:
                print("Premium Seat Selected")
    case 3:
            if age <= 5:
                print("Free Entry")
            else:
                print("VIP Seat Selected")