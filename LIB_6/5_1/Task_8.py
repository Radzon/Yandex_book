import numpy as np


def snake(n, m, direction='H'):
    if direction == 'V':
        n, m = m, n
    a = np.arange(1, n * m + 1, dtype='int16')
    a = a.reshape((m, n))
    for i in range(1, m, 2):
        a[i] = list(reversed(a[i]))
    if direction == 'V':
        a = a.transpose()
    return a


print(snake(5, 3, direction='H'))
