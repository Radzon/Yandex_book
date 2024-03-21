n = int(input())
q = 3
for i in range(n):
    k = q + i
    for j in range(k):
        print(f'До старта {k} секунд(ы)')
        k -= 1
    print(f'Старт {i + 1}!!!')
