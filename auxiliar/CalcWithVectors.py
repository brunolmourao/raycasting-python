import numpy as np
from numpy import linalg as LG

from estruturaDeDados.Point import Point

""" Para transformar lista num vetor mesmo
    a = [1, 2, 3] -> listas, python puro. NÃO se comportam como vetores
    a = np.array([1, 2, 3]) -> converte uma lista em vetor
"""


def produto_escalar(vetor1, vetor2):
    v1 = np.array(vetor1)
    v2 = np.array(vetor2)
    return np.sqrt(np.dot(v1, v2))


def produto_vetorial(vetor1, vetor2):
    return np.cross(vetor1, vetor2)


def norma(vetor):
    return produto_escalar(vetor, vetor)


def normalizar(vetor):
    n = LG.norm(vetor)
    return vetor / n


def diff(vetor1, vetor2):
    v1 = np.array(vetor1)
    v2 = np.array(vetor2)
    return v2 - v1


def vetor_entre_2_pontos(origem: Point, destino: Point):
    x = destino.x - origem.x
    y = destino.y - origem.y
    z = destino.z - origem.z
    return np.array([x, y, z])


# Calcula o Baricentro para as faces triangulares baseado nos seus pontos
def calc_baricentro(x1, x2, x3):
    baricentro_x = (x1.x + x2.x + x3.x) / 3
    baricentro_y = (x1.y + x2.y + x3.y) / 3
    baricentro_z = (x1.z + x2.z + x3.z) / 3
    return Point(baricentro_x, baricentro_y, baricentro_z)


# valida se os t encontrados são válidos baseados em seus pontos
def validar_faces_triangulares(p, p1, p2, p3):
    p1p2 = vetor_entre_2_pontos(p2, p1)
    p1p = vetor_entre_2_pontos(p, p1)
    p1p3 = vetor_entre_2_pontos(p3, p1)
    p2p3 = vetor_entre_2_pontos(p3, p2)
    p2p = vetor_entre_2_pontos(p, p2)
    p3p1 = vetor_entre_2_pontos(p1, p3)
    p3p = vetor_entre_2_pontos(p, p3)
    if produto_escalar(produto_vetorial(p1p2, p1p), produto_vetorial(p1p2, p1p3)) > 0:
        if produto_escalar(produto_vetorial(p2p3, p2p), produto_vetorial(p1p2, p1p3)) > 0:
            if produto_escalar(produto_vetorial(p3p1, p3p), produto_vetorial(p1p2, p1p3)) > 0:
                return True
    return False


def transform_camera(matrix, ponto):
    ponto1 = np.array([ponto.x, ponto.y, ponto.z])
    ponto1 = np.append(ponto1, [1])
    produto = np.dot(matrix, ponto1)
    # print(produto.item(0), produto.item(1), produto.item(2))
    return Point(produto.item(0), produto.item(1), produto.item(2))
