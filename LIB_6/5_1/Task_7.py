import numpy as np


def make_board(n):
    row = [0 if j % 2 else 1 for j in range(n)]
    a = np.array([row if i % 2 == 0 else list(reversed(row)) for i in range(n)], dtype='int8')
    return a