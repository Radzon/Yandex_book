price = float(input())
h = 0
while price != 0:
    if price >= 500:
        price = price * 0.9
        h += price
    else:
        h += price
    price = float(input())
print(h)