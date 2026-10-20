balance = 10000

while True:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposited. New balance: ₹", balance)
        else:
            print("Invalid amount. Must be greater than zero.")

    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))
        if amount <= 0:
            print("Invalid amount. Must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawn. New balance: ₹", balance)

    elif choice == "4":
        print("Thank you. Exiting.")
        break

    else:
        print("Invalid menu choice.")