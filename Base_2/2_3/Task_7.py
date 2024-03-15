A = int(input())
B = int(input())
a = A
b = B
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
ost_1 = A / a
ost_2 = B / b
r = ost_1 * ost_2 * a
print(int(r))