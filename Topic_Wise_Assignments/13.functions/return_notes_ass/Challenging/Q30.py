def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return f"{item} Total price: {(quantity*price)+delivery_fee}"

print(order_summary("Book", 6, 45, delivery_fee=39))