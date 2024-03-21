h = int(input())
w = int(input())
long = w * h + (h - 1)
for i in range(1, h + 1):
    for j in range(1, h + 1):
        if j == 1:
            print(f'{i * j:^{w}}', end='')
        else:
            print(f'|{i * j:^{w}}', end='')
    print()
    if i != h:
        print('-' * long)