number = str(input())
long = len(number)
numb = ''
for i in range(long):
    numb = number[::- 1]
if numb == number:
    print('YES')
else:
    print('NO')