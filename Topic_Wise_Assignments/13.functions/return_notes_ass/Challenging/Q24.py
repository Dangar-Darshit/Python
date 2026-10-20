def apply_discount(price, discount=0):
    if (0<=discount<=100):
        return price - ((price*discount)/100)

print(apply_discount(1000, 20))