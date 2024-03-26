import numpy as np


def multiplication_matrix(n):
    a = np.array([j * i for i in range(1, n + 1) for j in range(1, n + 1)])
    return a.reshape((n, n))
