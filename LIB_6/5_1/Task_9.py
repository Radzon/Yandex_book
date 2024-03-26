import numpy as np


def rotate(matx, degree):
    for i in range(degree // 90):
        matx = np.rot90(matx, -1)
    return matx


print(rotate(np.arange(12).reshape(3, 4), 90))