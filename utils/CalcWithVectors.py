import numpy as np

""" Para transformar lista num vetor mesmo
    a = [1, 2, 3] -> listas, python puro. NÃO se comportam como vetores
    a = np.array([1, 2, 3]) -> converte uma lista em vetor
"""

from geometricAttributes.Point import Point

def produto_escalar(vetor1: object, vetor2: object):
    return np.sqrt(np.dot(vetor1, vetor2))


def produto_vetorial(vetor1, vetor2):
    return np.cross(vetor1, vetor2)


def norma(vetor):
    return produto_escalar(vetor, vetor)


def normalizar(vetor):
    return vetor / norma(vetor)


def diff(vetor1, vetor2):
    return vetor2 - vetor1


def validar_faces_triangulares(p, p1, p2, p3):
    p1p = diff(p, p1)
    p2p = diff(p, p2)
    p3p = diff(p, p3)
    v1v2 = produto_vetorial(p1p, p2p)
    v2v3 = produto_vetorial(p2p, p3p)
    v3v1 = produto_vetorial(p3p, p1p)
    if produto_escalar(v1v2, v2v3) > 0:
        if produto_escalar(v1v2, v3v1) > 0:
            return True
    return False


def transform_camera(matrix, ponto):
    ponto1 = np.array([ponto.x, ponto.y, ponto.z])
    ponto1 = np.append(ponto1, [1])
    produto = np.dot(matrix, ponto1)
    # print(produto.item(0), produto.item(1), produto.item(2))
    return Point(produto.item(0), produto.item(1), produto.item(2))
