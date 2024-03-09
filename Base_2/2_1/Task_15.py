n = input()
n = n.split()
numb = []
for i in range(len(n)):
    numb.append(int(n[i]))
x1 = numb[0]
for j in range(1, len(numb)):
    x2 = numb[j]
    while x1 != x2:
        if x1 > x2:
            x1 = x1 - x2
        else:
            x2 = x2 - x1
print(x1)