n = int(input())
k = 1
j = 1
while k <= n:
    for i in range(k, k + j):
        if i <= n:
            print(i, end=' ')
    k += j
    j += 1
    print()