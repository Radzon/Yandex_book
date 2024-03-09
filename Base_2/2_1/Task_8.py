numb = int(input())
for i in range(numb):
    words = input()
    inx = words.find('зайка')
    if inx >= 0:
        print(inx + 1)
    else:
        print('Заек нет =(')