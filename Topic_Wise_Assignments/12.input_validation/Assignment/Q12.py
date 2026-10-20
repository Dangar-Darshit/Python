bal = 2000

amt = int(input("Enter your deposit amount: "))

while amt < 0:
    amt = int(input("Enter valid amount: "))
else:
    bal += amt

print("New Balance:", bal)