numb = int(input())
n = 1
if numb == 0:
    print(1)
else:
    for i in range(1, numb + 1):
        n *= i
print(n)