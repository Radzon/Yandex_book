n = int(input())
q = 0
for i in range(n):
    word = ''
    flag = False
    while word != 'ВСЁ':
        word = input()
        if 'зайка' in word:
            flag = True
    if flag:
        q += 1
print(q)