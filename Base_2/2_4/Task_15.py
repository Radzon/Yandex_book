h = int(input())
w = int(input())
numb = 1
k = (h * 2) - 1
c = 1
d = len(str(h * w))
for i in range(1, h + 1):
    numb = i
    for j in range(1, w + 1):
        print(f'{numb:>{d}}', end=' ')
        if j % 2 == 0:
            numb += c
        else:
            numb += k
    print()
    k -= 2
    c += 2