convt = int(input("""Convert to:-
1 → Kilometers to Meters
2 → Meters to Kilometers
3 → Kilograms to Grams
4 → Grams to Kilograms
Enter choice: """))
value = int(input("Enter Value: "))

match convt:
    case 1:
        print(value * 1000, "m")
    case 2:
        print(value/1000, "km")
    case 3:
        print(value * 1000, "gm")
    case 4:
        print(value/1000, "kg")