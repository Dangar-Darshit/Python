balance = 10000

amount = int(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance or amount % 100 != 0:
    if amount <= 0:
        print("Amount must be positive.")
    elif amount > balance:
        print("Amount exceeds balance.")
    else:
        print("Amount must be a multiple of ₹100.")
    amount = int(input("Enter withdrawal amount: "))

balance -= amount
print("Withdrawn: ₹", amount)
print("Remaining balance: ₹", balance)