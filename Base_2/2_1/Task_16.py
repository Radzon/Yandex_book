n = int(input())
numb = int(input())
data = []
quatity = 0
for i in range(numb):
    string = input()
    quatity += len(string)
    data.append(list(string))
q = 0
if quatity > n:
    for i in range(numb):
        s = data[i]
        if q >= (n - 3):
            break
        for j in range(len(s)):
            if q < (n - 3):
                print(s[j], end='')
                q += 1
        if q < (n - 3):
            print()
    print('...')
else:
    for c in range(numb):
        print(''.join(data[c]))