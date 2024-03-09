n = int(input())
numbs = []
for i in range(n):
    numbs.append(int(input()))
q = int(input())
for x in range(len(numbs)):
    print(numbs[x] ** q)