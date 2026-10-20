menu = int(input("""<---Restaurant Ordering System--->
Login With:-
1 → Starters
2 → Main Course
3 → Desserts
4 → Drinks
User Role: """))

match menu:
    case 1:
        starters = int(input("You want to order:\n1 → Soup\n2 → Spring Roll\n3 → Garlic Bread\nYour choice: "))
        match starters:
            case 1:
                print("Confirming Soup")
            case 2:
                print("Confirming Spring Roll")
            case 3:
                print("Confirming Garlic Bread")
    case 2:
            main = int(input("You want to order:\n1 → Pizza\n2 → Pasta\n3 → Biryani\nYour choice: "))
            match main:
                case 1:
                    print("Confirming Pizza")
                case 2:
                    print("Confirming Pasta")
                case 3:
                    print("Confirming Biryani")
    case 3:
            desserts = int(input("You want to order:\n1 → Ice Cream\n2 → Cake\n3 → Gulab Jamun\nYour choice: "))
            match desserts:
                case 1:
                    print("Confirming Ice-Cream")
                case 2:
                    print("Confirming Cake")
                case 3:
                    print("Confirming Gulab Jamun")
    case 4:
                drinks = int(input("You want to order:\n1 → Pizza\n2 → Pasta\n3 → Biryani\nYour choice: "))
                match drinks:
                    case 1:
                        print("Confirming Coffee")
                    case 2:
                        print("Confirming Tea")
                    case 3:
                        print("Confirming Juice")