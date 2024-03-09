alpha = {}
s = input()
while s != 'ФИНИШ':
    s = s.lower()
    for x in s:
        if x.isalpha():
            alpha[x] = alpha.get(x, 0) + 1
    s = input()
print(max(sorted(alpha), key=lambda x: alpha[x]))