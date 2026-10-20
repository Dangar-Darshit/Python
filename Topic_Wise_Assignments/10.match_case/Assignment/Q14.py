priority = int(input("""<---Customer Support Priority--->
1 → Low
2 → Medium
3 → High
4 → Critical
Your number : """))

match priority:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
        print("Urgent Priority")