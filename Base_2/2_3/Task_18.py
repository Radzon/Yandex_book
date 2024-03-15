numb = int(input())
i = 2
while numb > 1:
    if numb % i == 0:
        print(i, end=' ')
        numb //= i
        if numb > 1:
            print('*', end=' ')
    else:
        i += 1