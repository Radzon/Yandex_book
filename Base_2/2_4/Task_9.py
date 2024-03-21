n = int(input())
sum = ''
for i in range(n):
    count = '0'
    numb = input()
    for i in range(len(numb)):
        if int(numb[i]) > int(count):
            count = numb[i]
    sum += count
print(sum)