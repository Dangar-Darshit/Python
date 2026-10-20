menu = int(input("""Menu Choice:\n
1. View profile
2. Edit profile
3. Settings
4. Exit

Enter your choice: """))

while menu < 1 or menu > 4:
    menu = int(input("""Menu Choice:\n
1. View profile
2. Edit profile
3. Settings
4. Exit

Enter Valid choice: """))

if menu == 4:
    print("Exiting...")
else:
    print("\nOpening...")