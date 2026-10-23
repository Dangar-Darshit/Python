total_revenue = 0

for i in range(6):
    units = int(input("Enter units: "))
    bill = 0

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 400:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        bill = 100 * 5 + 100 * 7 + 200 * 10 + (units - 400) * 15

    print("Bill:", bill)
    total_revenue += bill

    if bill < 1000:
        print("Low")
    elif bill <= 3000:
        print("Medium")
    else:
        print("High")

print("Total revenue:", total_revenue)