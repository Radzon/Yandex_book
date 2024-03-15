numb = input()
s = 0
for i in range(len(numb)):
    if int(numb[i]) > s:
        s = int(numb[i])
    else:
        pass
    i += 1
print(s)