import numpy as np
from estruturaDeDados import Point

""" Para transformar lista num vetor mesmo
    a = [1, 2, 3] -> listas, python puro. NÃO se comportam como vetores
    a = np.array([1, 2, 3]) -> converte uma lista em vetor
"""


def produto_escalar(vetor1, vetor2):
    v1 = np.array(vetor1)
    v2 = np.array(vetor2)
    return np.sqrt(np.dot(v1, v2))


def produto_vetorial(vetor1, vetor2):
    v1 = np.array(vetor1)
    v2 = np.array(vetor2)
    return np.cross(v1, v2)


def norma(vetor):
    return produto_escalar(vetor, vetor)


def normalizar(vetor):
    v = np.array(vetor)
    v / norma(vetor)


def diff(vetor1, vetor2):
    v1 = np.array(vetor1)
    v2 = np.array(vetor2)
    return v2 - v1


def vetor_entre_2_pontos(origem: Point, destino: Point):
    x = destino.x - origem.x
    y = destino.y - origem.y
    z = destino.z - origem.z
    return np.array([x, y, z])
