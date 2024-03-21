n = int(input())
max_n = 0
won = ''
for i in range(n):
    sum = 0
    name = input()
    numb = input()
    for i in range(len(numb)):
        sum = sum + int(numb[i])
    if sum >= max_n:
        max_n = sum
        won = name
print(won)