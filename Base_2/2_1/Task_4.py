s = input()
string_s = []
while s != '':
    if s[-3:] == '@@@':
        pass
    elif s[:2] == '##':
        string_s.append(s[2:])
    else:
        string_s.append(s)
    s = input()
for i in range(len(string_s)):
    print(string_s[i])