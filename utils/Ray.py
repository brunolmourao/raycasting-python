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
from geometricAttributes.Point import Point


class Ray:
    # Método Construtor
    def __init__(self, p, v_direcao):
        self.__p = p
        self.__v_direcao = v_direcao / np.linalg.norm(v_direcao)

    def ponto(self, t: float):
        temp_p = self.p.coords()
        v = temp_p + t * self.__v_direcao
        p = Point(v[0], v[1], v[2])
        return p

    # Método getters
    @property
    def p(self):
        return self.__p

    @property
    def v_direcao(self):
        return self.__v_direcao
