store = int(input("""<---Store Discount Category--->
1 → Bronze
2 → Silver
3 → Gold
4 → Platinum
Your Level : """))

match store:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")