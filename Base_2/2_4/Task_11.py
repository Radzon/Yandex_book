numb = int(input())
count = 0
for i in range(numb):
    x = int(input())
    if x == 1:
        pass
    else:
        for j in range(2, x):
            if x % j == 0:
                break
        else:
            count += 1
print(count)