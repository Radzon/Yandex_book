h = int(input())
w = int(input())
numb = 1
d = len(str(h * w))
for i in range(h):
    for j in range(w):
        print(f'{numb:>{d}}', end=' ')
        numb += 1
    print()