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


class Cone:
    __theta = 0

    # TODO: cálculo de theta. Verificar se o que esta comentado esta correto
    # Método Construtor
    def __init__(self, vertice, v_direcao, altura, raio):
        self.__vertice = np.array(vertice)
        self.__v_direcao = np.array(v_direcao)
        self.__altura = altura
        self.__raio = raio
        # p_raio = np.array([raio, 0, 0])
        # geratriz = vertice - p_raio
        # self.theta = altura/np.linalg.norm(geratriz)

    # TODO: implementar equação do clindro
    @staticmethod
    def contem(t):
        """equação do cone"""
        """t: float.
                t aplicado na equação gera o ponto 
        """

    # TODO: implementar a equação de interseção com a reta
    @staticmethod
    def intersection_with(self, reta):
        """retona uma lista com os t's dos pontos, se exitirem.
        """
        t1 = 0
        t2 = 0
        return []

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
