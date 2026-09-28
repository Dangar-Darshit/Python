cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if cost_price <= 0:
    print("Invalid cost price")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    percentage = (profit / cost_price) * 100
    print("Profit =", profit)
    print("Profit Percentage =", percentage)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    percentage = (loss / cost_price) * 100
    print("Loss =", loss)
    print("Loss Percentage =", percentage)
else:
    print("No profit and no loss")
