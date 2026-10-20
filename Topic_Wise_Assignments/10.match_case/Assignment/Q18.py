e = int(input("Select one:-\n1. Electronics\n2. Clothing\n Enter -> "))
match e:
    case 1:
        ele = int(input("Select from below:-\n1 → Mobile\n2 → Laptop\n3 → Headphones\n Enter -> "))
        match ele:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop SElected")
            case 3:
                print("Headphones Selected")
    case 2:
        clt = int(input("Select from below1 → Shirt\n2 → Jeans\n3 → Shoes\nEnter: "))
        match clt:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")