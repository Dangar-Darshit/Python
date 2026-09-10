units = float(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity Bill =", bill)
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print("Electricity Bill =", bill)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print("Electricity Bill =", bill)
