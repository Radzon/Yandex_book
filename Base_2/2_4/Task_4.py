n = int(input())
q = 0
for i in range(n):
    j = input()
    for s in range(len(j)):
        q = q + int(j[s])
print(q)