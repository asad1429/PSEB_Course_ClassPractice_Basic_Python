products = [("Laptop", 150000, 3), ("Mouse", 2500, 0),
("Keyboard", 5000, 12), ("Monitor", 45000, 2)]

for name, price, quantity in products:
    if quantity > 0:
        print(f"{name} is available.")
    else:
        print(f"{name} is out of stock.")