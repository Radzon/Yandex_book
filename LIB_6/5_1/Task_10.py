import numpy as np


def stairs(matx):
    dlina = matx.size
    res = np.zeros((dlina, dlina))
    for i in range(dlina):
        res[i] = matx
        temp = matx[-1]
        for j in range(1, dlina):
            matx[-j] = matx[-j - 1]
        matx[0] = temp
    return res.astype(int)


print(stairs(np.arange(3)))
