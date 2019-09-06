import numpy as np

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


def normalizar(vetor):
    vetor / norma(vetor)


def diff(vetor1, vetor2):
    return vetor2 - vetor1
