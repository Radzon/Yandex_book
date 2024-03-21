n = int(input())
x1 = int(input())
for i in range(n - 1):
    x2 = int(input())
    while x1 != x2:
        if x1 > x2:
            x1 = x1 - x2
        else:
            x2 = x2 - x1
print(x1)