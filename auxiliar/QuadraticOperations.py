"""
Classe que calcula operações básicas para os problemas, como delta, normalização, dentre outras

"""
import numpy as np


def delta(a, b, c):
    return b * b - 4 * a * c


def roots(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        return [0]
    elif d == 0:
        return [-1 * b / 2 * a]
    else:
        return [-1 * b + np.sqrt(d) / 2 * a, -1 * b + np.sqrt(d) / 2 * a]
