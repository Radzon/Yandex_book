ot = ''
max_n = 1001
min_n = 0
while ot != 'Угадал!':
    print(int((max_n - min_n) / 2 + min_n))
    ot = input()
    if 'Меньше' in ot:
        max_n = (max_n - min_n) // 2 + min_n
    elif 'Больше' in ot:
        min_n = (max_n - min_n) // 2 + min_n
    else:
        pass