import math

numbs = list(map(float, input().split()))
print(math.prod(numbs) ** (1 / len(numbs)))
