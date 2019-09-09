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

from utils.CalcWithVectors import diff
from utils.CalcWithVectors import produto_escalar
from utils.QuadraticOperations import roots
from geometricAttributes.Point import Point


class Cone:
    __theta = 0

    # TODO: cálculo de theta. Verificar se o que esta comentado esta correto
    def __init__(self, centro_base, raio, altura, v_direcao):
        self.__vertice = Point(centro_base.x, centro_base.y + altura, centro_base.z)
        self.__v_direcao = np.array(v_direcao)
        self.__altura = altura
        self.__raio = raio

    # TODO: implementar a equação de interseção com a reta

    def intersection_with(self, reta):
        p_raio = np.array([self.__raio, 0, 0])
        geratriz = self.__vertice.coords() - p_raio
        theta = self.__altura / np.linalg.norm(geratriz)
        v = self.__vertice.coords() - reta.p.to_array()

        a = np.power(produto_escalar(reta.v_direcao.coords(), self.__v_direcao, 2)) - \
            produto_escalar(reta.v_direcao.coords(), reta.v_direcao.coords()) * np.power(
            np.cos(theta), 2)
        b = np.power(produto_escalar(v, reta.v_direcao.to_array()), 2) * np.power(np.cos(theta), 2) - produto_escalar(
            v, self.__v_direcao) * produto_escalar(reta.v_direcao.to_array(), self.__v_direcao)
        c = np.power(produto_escalar(v, self.__v_direcao), 2) - produto_escalar(v, v) * np.power(
            np.cos(theta), 2)
        # Adicionando validação da Altura
        tint = roots(a, b, c)
        index = 0
        for x in tint:
            p = reta.ponto(x)
            if p[1] > self.__altura:
                tint.pop(index)
            else:
                index = index + 1
        return tint

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
