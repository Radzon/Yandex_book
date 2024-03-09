n = int(input())
s = []
for i in range(n):
    s.append(input())
find = input()
for x in s:
    if find.lower() in x.lower():
        print(x)