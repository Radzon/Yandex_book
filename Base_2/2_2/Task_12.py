n1 = int(input())
n2 = int(input())
n3 = int(input())
max_n = max(n1, n2, n3)
min_n = min(n1, n2, n3)
sr = (n1 + n2 + n3) - max_n - min_n
if max_n < min_n + sr:
    print('YES')
else:
    print('NO')