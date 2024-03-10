peta = int(input())
vasa = int(input())
tola = int(input())

if (max(peta, vasa, tola) == peta):
    print('1.', 'Петя')
elif (max(peta, vasa, tola) == vasa):
    print('1.', 'Вася')
else:
    print('1.', 'Толя')

if ((vasa < peta < tola) or (tola < peta < vasa)):
    print('2.', 'Петя')
elif ((peta < vasa < tola) or (tola < vasa < peta)):
    print('2.', 'Вася')
else:
    print('2.', 'Толя')

if (min(peta, vasa, tola) == peta):
    print('3.', 'Петя')
elif (min(peta, vasa, tola) == vasa):
    print('3.', 'Вася')
else:
    print('3.', 'Толя')