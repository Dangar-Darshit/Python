weather = input("""<---Weather Advice--->
sunny
rainy
cloudy
snowy
Enter Weather : """).lower()

match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothes")
    case _:
        print("Unknown Weather")