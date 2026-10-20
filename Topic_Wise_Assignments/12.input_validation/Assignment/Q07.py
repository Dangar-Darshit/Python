balance = 5000
amt = int(input("Enter your withdraw amount: "))
for i in (1,amt+1):
    if amt < 0 or amt < balance:
        amt = int(input("Enter your withdraw amount: "))
    balance -= i
print("Remaining balance: balance:", balance)