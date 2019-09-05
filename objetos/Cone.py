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

from auxiliar.CalcWithVectors import produto_escalar
from auxiliar.QuadraticOperations import roots


class Cone:
    __theta = 0

    # TODO: cálculo de theta. Verificar se o que esta comentado esta correto
    def __init__(self, centro_base, raio, altura, v_direcao):
        """

        :rtype: object
        """
        self.__vertice = centro_base
        self.__v_direcao = v_direcao
        self.__altura = altura
        self.__raio = raio
        self.__cor = '_'

    def intersection_with(self, reta):
        """retorna uma lista com os t's dos pontos, se exitirem.
        """
        p_raio = np.array([self.__raio, 0, 0])
        geratriz = self.__vertice.to_array() - p_raio
        theta = self.__altura / np.linalg.norm(geratriz)
        v = self.__vertice.to_array() - reta.p.to_array()

        a = np.power(produto_escalar(reta.v_direcao.to_array(), self.__v_direcao.to_array()), 2) - \
            produto_escalar(reta.v_direcao.to_array(), reta.v_direcao.to_array()) * np.power(
            np.cos(theta), 2)
        b = np.power(produto_escalar(v, reta.v_direcao.to_array()), 2) * np.power(np.cos(theta), 2) - produto_escalar(
            v, self.__v_direcao.to_array()) * produto_escalar(reta.v_direcao.to_array(), self.__v_direcao.to_array())
        c = np.power(produto_escalar(v, self.__v_direcao.to_array()), 2) - produto_escalar(v, v) * np.power(np.cos(theta), 2)

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

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor
