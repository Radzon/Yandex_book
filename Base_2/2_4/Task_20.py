n = int(input())
max_ss = 0
max_sum = 0
for i in range(2, 11):
    digit_sum = 0
    x = n
    while x > 0:
        digit_sum += x % i
        x //= i
    if max_sum < digit_sum:
        max_sum = digit_sum
        max_ss = i
print(max_ss)