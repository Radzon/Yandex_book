numb = input()
k = ''
for i in range(len(numb)):
    if (int(numb[i]) / 2) % 1 != 0:
        k = k + numb[i]
    else:
        pass
    i += 1
print(k)