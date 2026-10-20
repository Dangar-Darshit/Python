while True:
    quantity = int(input("Enter quantity (positive integer): "))
    if quantity > 0:
        break
    print("Invalid quantity. Please try again.")

while True:
    price = int(input("Enter unit price (greater than zero): "))
    if price > 0:
        break
    print("Invalid price. Please try again.")

total = quantity * price
print("Total cost: ₹", total)