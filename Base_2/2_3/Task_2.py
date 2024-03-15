t = ''
count = 0
while t != 'Приехали!':
    t = input()
    if 'зайка' in t:
        count += 1
print(count)