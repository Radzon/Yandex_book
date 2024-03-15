a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b == 0:
        if c == 0:
            print('Infinite solutions')
        else:
            print('No solution')
    else:
        print(-c / b)
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('No solution')
    elif d == 0:
        print(-b / (a * 2))
    else:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)