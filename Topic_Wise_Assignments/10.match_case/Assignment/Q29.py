lib = int(input("""<-----Library Management System----->
Select from below:-
1 → Search Book
2 → Issue Book
3 → Return Book
4 → View Issued Books
5 → Exit
Enter your choice: """))

match lib:
    case 1:
        print("Search Book Selected")
    case 2:
        print("Issue Book Selected")
    case 3:
        print("Return Book Selected")
    case 4:
        print("View Issued Books Selected")
    case 5:
        print("Exiting...")
    case _:
        print("Invalid Selection")