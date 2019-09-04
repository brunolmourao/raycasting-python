"""
Classe define o objeto Cone Reto
Atributos:
    vertice: Ponto
        Vértice do cone;
    v_direcao: Vetor
        Vetor unitário que define a direção do eixo do cone;
    theta: float
        é o ângulo entre a geratriz	e o	eixo do	cone;
    altura: float
        A altura do	cone;
    raio: float
        Raio da base do cone.
"""
import numpy as np

from auxiliar.CalcWithVectors import diff
from auxiliar.CalcWithVectors import produto_escalar
from estruturaDeDados.Point import Point
from auxiliar.QuadraticOperations import roots


class Cone:
    __theta = 0

    # TODO: cálculo de theta. Verificar se o que esta comentado esta correto
    def __init__(self, centro_base, raio, altura, v_direcao):
        self.__vertice = np.array(centro_base)
        self.__v_direcao = np.array(v_direcao)
        self.__altura = altura
        self.__raio = raio

    # TODO: implementar a equação de interseção com a reta
    @staticmethod
    def intersection_with(self, reta):
        """retona uma lista com os t's dos pontos, se exitirem.
        """
        p_raio = np.array([self.__raio, 0, 0, 0])
        geratriz = self.__vertice - p_raio
        theta = self.__altura/np.linalg.norm(geratriz)
        v = self.__vertice - reta.p

        a = np.power([produto_escalar(reta.v_normal, self.__v_direcao)], 2) - produto_escalar(reta.v_normal, reta.v_normal) * np.power([np.cos(theta)], 2)
        b = np.power([produto_escalar(v, reta.v_normal)], 2) * np.power([np.cos(theta)], 2) - produto_escalar(v, self.__v_direcao) * produto_escalar(reta.v_normal, self.__v_direcao)
        c = np.power([produto_escalar(v, self.__v_direcao)], 2) - produto_escalar(v, v) * np.power([np.cos(theta)], 2)

        return roots(a, b, c)

    # Método getters
    @property
    def vertice(self):
        return self.__vertice

    @property
    def altura(self):
        return self.__altura

    @property
    def theta(self):
        return self.__theta

    @property
    def raio(self):
        return self.__raio

    @property
    def v_direcao(self):
        return self.__v_direcao

    # Métodos setter
    @vertice.setter
    def vertice(self, v):
        self.vertice = v

    @v_direcao.setter
    def v_direcao(self, v):
        self.__v_direcao = v

    @altura.setter
    def altura(self, a):
        self.__altura = a

    @theta.setter
    def theta(self, t):
        self.__theta = t

    @raio.setter
    def raio(self, r):
        self.__raio = r
