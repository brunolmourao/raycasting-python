import numpy as np
from geometricAttributes import Point

def transform_to_camera(matrix, ponto):
    # ponto1 = np.array([ponto.x, ponto.y, ponto.z])
    ponto1 = np.append(ponto, [1])
    produto = np.dot(matrix, ponto1)
    # print(produto.item(0), produto.item(1), produto.item(2))
    return Point(produto.item(0), produto.item(1), produto.item(2))