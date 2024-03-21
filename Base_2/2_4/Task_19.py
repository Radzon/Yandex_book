n = int(input())
if n == 1:
    print(1)
else:
    if type(n / 2) is float:
        x = int(int(n + 1) / 2)
    else:
        x = n / 2

    s = [[1] * n for _ in range(n)]

    num_now = 1

    for center_size in range(1, x):
        num_now += 1
        for i in range(center_size, n - center_size):
            s[center_size][i] = num_now
            s[n - center_size - 1][i] = num_now
            s[i][center_size] = num_now
            s[i][n - center_size - 1] = num_now
    for line in s:
        print(' '.join(f'{str(line[i]):>{len(str(x))}}' for i in range(n)))