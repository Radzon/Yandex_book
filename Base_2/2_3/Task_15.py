total = int(input())
how = 0
for i in range(total):
    text = input()
    if 'зайка' in text:
        how += 1
    else:
        pass
print(how)