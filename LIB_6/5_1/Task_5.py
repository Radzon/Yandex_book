import math

a = (map(float, input().split()))
b = input().split()
b = (float(b[0]) * math.cos(float(b[1])), float(b[0]) * math.sin(float(b[1])))
print(math.dist(a, b))
