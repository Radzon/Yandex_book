numb_string = input()
flag = True
x = 0
while flag:
    s = 0
    if numb_string[x] == '0':
        while x < len(numb_string) and numb_string[x] == '0':
            s += 1
            x += 1
        print('0', s)
    else:
        while x < len(numb_string) and numb_string[x] == '1':
            s += 1
            x += 1
        print('1', s)
    if x >= len(numb_string):
        flag = False