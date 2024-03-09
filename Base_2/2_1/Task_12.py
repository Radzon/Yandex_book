kasha = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
n = int(input())
k = 0
for i in range(n):
    if k >= len(kasha):
        k = 0
    print(kasha[k])
    k += 1
