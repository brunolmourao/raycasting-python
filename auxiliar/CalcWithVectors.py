import numpy as np
from estruturaDeDados import Point

""" Para transformar lista num vetor mesmo
    a = [1, 2, 3] -> listas, python puro. NÃO se comportam como vetores
    a = np.array([1, 2, 3]) -> converte uma lista em vetor
"""


def produto_escalar(vetor1: object, vetor2: object):
    return np.sqrt(np.dot(vetor1, vetor2))


def produto_vetorial(vetor1, vetor2):
    return np.cross(vetor1, vetor2)


def norma(vetor):
    return produto_escalar(vetor, vetor)


@staticmethod
def normalizar(vetor):
    vetor / norma(vetor)


def diff(vetor1, vetor2):
    return vetor2 - vetor1


def vetor_entre_2_pontos(origem: Point, destino: Point):
    return np.array(destino.x - origem.x, destino.y - origem.y, destino.z - origem.z)
