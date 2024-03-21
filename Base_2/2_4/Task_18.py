n = int(input())
num = 1
count = 1
max_length = 0
while num <= n:
    length = -1
    for j in range(count):
        if num > n:
            break
        length += 1
        num_copy = num
        while num_copy > 0:
            length += 1
            num_copy //= 10
        num += 1
    count += 1
    max_length = max(max_length, length)
num = 1
count = 1
while num <= n:
    num_start = num
    length = -1
    for j in range(count):
        if num > n:
            break
        length += 1
        num_copy = num
        while num_copy > 0:
            length += 1
            num_copy //= 10
        num += 1
    num = num_start
    left = (max_length - length) // 2
    right = max_length - length - left
    print(" " * left, end="")
    for j in range(count):
        if num > n:
            break
        print(num, end=" ")
        num += 1
    print(" " * (right - 1))
    count += 1