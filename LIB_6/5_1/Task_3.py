import math

a, b = list(map(int, input().split()))
if a > b:
    print(int(math.factorial(a - 1) / (math.factorial(b - 1) * math.factorial(a - b))), math.comb(a, b))
else:
    print(1, 1)
# не робит