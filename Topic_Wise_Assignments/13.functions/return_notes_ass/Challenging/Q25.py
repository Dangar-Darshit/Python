def calculate_pay(hours, rate=200, bonus=0):
    pay = hours * rate + bonus
    return pay

print(calculate_pay(2, 350, 20))