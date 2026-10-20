s = int(input("Enter number of selecting mobile mr=enu from below:-\n1. Wi-Fi\n2.Bluetooth\n3. Mobile Data\n4. Airplane Mode\n5. Exit\nYour setting no.-> "))
match s:
    case 1:
        print("Wi-Fi Selected")
    case 2:
        print("Bluetooth Selected")
    case 3:
        print("Mobile Data Selected")
    case 4:
        print("Airplane Mode Selected")
    case 5:
        print("Exited from settings")
    case _:
        print("Invalid Settings")