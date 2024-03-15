direct = input()
wert = 0
hor = 0
while direct != 'СТОП':
    range = int(input())
    if direct == 'СЕВЕР':
        wert += range
    elif direct == 'ВОСТОК':
        hor += range
    elif direct == 'ЮГ':
        wert -= range
    else:
        hor -= range
    direct = input()
print(wert)
print(hor)
