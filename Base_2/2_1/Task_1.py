n = int(input())
out = 'YES'
for i in range(n):
    word = input()
    w = word[0]
    if 'а' == w or 'б' == w or 'в' == w:
        pass
    else:
        out = 'NO'
print(out)