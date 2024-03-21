h = int(input())
w = int(input())
numb = 1
d = len(str(h * w))
for i in range(h):
    for j in range(w):
        k = numb + (h * j)
        print(f'{k}'.rjust(d), end=' ')
    numb += 1
    print()