h = int(input())
w = int(input())
numb = 1
k = w
d = len(str(h * w))
for i in range(h):
    if i % 2 == 0:
        for j in range(i * w + 1, k + 1):
            print(f'{j:>{d}}', end=' ')
    else:
        for j in range(k, i * w, -1):
            print(f'{j:>{d}}', end=' ')
    k += w
    print()