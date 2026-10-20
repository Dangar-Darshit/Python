veg = int(input("Enter your choice\n1 → Vegetarian\n2 → Non-Vegetarian\n Enter: "))
match veg:
    case 1:
        vege = int(input("Select from below:- 1 → Paneer\n2 → Dal\n3 → Veg Biryani\n Enter: "))
        match vege:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani")
    case 2:
        nveg = int(input("Select from below:-\n 1 → Chicken Biryani\n2 → Chicken Curry\n3 → Fish Fry\n Enter: "))
        match nveg:
            case 1:
                print("Chicken Biryani")
            case 2:
                print("Chicken Curry")
            case 3:
                print("Fish Fry")