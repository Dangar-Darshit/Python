budget = 0
regular = 0
premium = 0
luxury = 0
total = 0

for i in range(8):
    price = int(input("Enter price: "))
    total = total + price
    if price < 500:
        print("Budget")
        budget = budget + 1
    elif price < 2000:
        print("Regular")
        regular = regular + 1
    elif price < 5000:
        print("Premium")
        premium = premium + 1
    else:
        print("Luxury")
        luxury = luxury + 1

print("Total:", total)
print("Average:", total / 8)
print("Budget:", budget, "Regular:", regular, "Premium:", premium, "Luxury:", luxury)