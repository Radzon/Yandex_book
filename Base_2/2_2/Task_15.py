numb = int(input())
n1 = numb // 10
n2 = numb % 10
numb2 = int(input())
n12 = numb2 // 10
n22 = numb2 % 10
max_n = max(n1, n2, n12, n22)
min_n = min(n1, n2, n12, n22)
sr = ((n1 + n2 + n12 + n22) - max_n - min_n) % 10
print(f'{max_n}{sr}{min_n}')
