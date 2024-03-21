n = int(input())
out = 0
for i in range(n):
    p = str(input())
    q = ''
    d = len(p)
    for j in range(d):
        q += p[d - (j + 1)]
    if q == p:
        out += 1
print(out)