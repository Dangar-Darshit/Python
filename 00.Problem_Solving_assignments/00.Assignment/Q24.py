amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
else:
    if amount < 500:
        discount_percentage = 0
    elif amount < 1000:
        discount_percentage = 5
    elif amount < 2000:
        discount_percentage = 10
    elif amount < 5000:
        discount_percentage = 15
    else:
        discount_percentage = 20

    discount_amount = amount * discount_percentage / 100
    final_amount = amount - discount_amount

    print("Original amount:", amount)
    print("Discount percentage:", discount_percentage, "%")
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
