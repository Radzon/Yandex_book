peta = int(input())
vasa = int(input())
tola = int(input())
if (max(peta, vasa, tola) == peta):
    print('          Петя')
elif (max(peta, vasa, tola) == vasa):
    print('          Вася')
else:
    print('          Толя')
if ((vasa < peta < tola) or (tola < peta < vasa)):
    print('  Петя')
elif ((peta < vasa < tola) or (tola < vasa < peta)):
    print('  Вася')
else:
    print('  Толя')
if (min(peta, vasa, tola) == peta):
    print('                  Петя')
elif (min(peta, vasa, tola) == vasa):
    print('                  Вася')
else:
    print('                  Толя')
print('   II      I      III   ')