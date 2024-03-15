start = int(input())
finish = int(input())
string = ''

if start > finish:
    ratio = -1
else:
    ratio = 1

finish_m = finish + ratio

for i in range(start, finish + ratio, ratio):
    string = string + str(i) + ' '
print(string)
