from sys import stdin
import math

for line in stdin:
    print(math.gcd(*(map(int, (line.rstrip("\n").split())))))

