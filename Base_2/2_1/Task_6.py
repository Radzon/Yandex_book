numb = int(input())
zai = 0
for i in range(numb):
    words = input()
    words.split()
    zai += words.count('зайка')
print(zai)