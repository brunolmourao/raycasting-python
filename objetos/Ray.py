"""""
Classe do Objeto Raio.
A classe Raio representa uma reta que tem inicio em P0 e direção dada pelo vetor n
Atributos:
    __p: Ponto
        Ponto que pertence a reta.
    __v_normal: Vetor
        Vetor Unitario que determina a direção da reta
"""

import numpy as np

from estruturaDeDados.Point import Point


class Ray:
    # Método Construtor
    def __init__(self, p: Point, v_normal: Point):
        self.__p = p
        self.__v_direcao = v_normal

    def ponto(self, t: float):
        temp_p = np.array([self.p.x, self.p.y, self.p.z])
        temp_v_direcao = np.array([self.v_direcao.x, self.v_direcao.y, self.v_direcao.z])
        v = temp_p + t * temp_v_direcao
        p = Point(v[0], v[1], v[2])
        return p

    def v_direcao_array(self):
        return np.array([self.v_direcao.x, self.v_direcao.y, self.v_direcao.z])

    # Método getters
    @property
    def p(self):
        return self.__p

    @property
    def v_direcao(self):
        return self.__v_direcao
