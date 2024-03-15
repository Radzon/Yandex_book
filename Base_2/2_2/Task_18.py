numb_1 = int(input())
numb_2 = int(input())
numb_3 = int(input())
c = max(numb_1, numb_2, numb_3)
b = min(numb_1, numb_2, numb_3)
a = (numb_1 + numb_2 + numb_3) - c - b
if (c ** 2) < (a ** 2 + b ** 2):
    print('крайне мала')
elif (c ** 2) > (a ** 2 + b ** 2):
    print('велика')
else:
    print('100%')