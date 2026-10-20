hospital = int(input("""Enter department:-
1 → General Medicine
2 → Cardiology
3 → Orthopedics
4 → Pediatrics
5 → Emergency
Department No.: """ ))

match hospital:
    case 1:
        print("General Medicine Department Selected")
    case 2:
        print("Cardiology Department Selected")
    case 3:
        print("Orthopedics Department Selected")
    case 4:
        print("Pediatrics Department Selected")
    case 5:
        print("Emergency Department Selected")
    case _:
        print("Invalid Department")