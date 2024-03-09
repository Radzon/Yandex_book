s = input()
while s != '':
    if s[0] == '#':
        pass
    elif '#' in s:
        print(s[:s.find('#')])
    else:
        print(s)
    s = input()