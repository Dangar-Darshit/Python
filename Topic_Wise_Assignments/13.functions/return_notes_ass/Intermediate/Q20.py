def bill(item, quantity=1, price=100):
    return quantity * price



print(bill("Notebook"))
print(bill("Pen", 3))  
print(bill("Eraser", price=50))
print(bill("Marker", 4, 25))  
print(bill(item="Folder", price=40, quantity=2))  