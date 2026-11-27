prices = [450, 1200, 300, 980, 75, 700, 25]

high = 0
lower = prices[0]

for price in prices:
    if price >= high:
        high = price
    if price < lower:
        lower = price

print(f"The Highest price is {high}.")
print(f"The Lowest price is {lower}.")
