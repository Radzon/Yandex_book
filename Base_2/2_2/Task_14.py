numb = int(input())
n1 = numb // 100
n2 = numb // 10 % 10
n3 = numb % 10
max_n = max(n1, n2, n3)
min_n = min(n1, n2, n3)
sr = (n1 + n2 + n3) - max_n - min_n
if min_n == 0:
    print(f'{sr}{min_n} {max_n}{sr}')
else:
    print(f'{min_n}{sr} {max_n}{sr}')