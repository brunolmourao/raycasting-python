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

from utils.CalcWithVectors import produto_escalar
from utils.QuadraticOperations import roots


class Cone:

    def __init__(self, centro_base, raio, altura, v_direcao):
        self.__vertice = centro_base.coords() + altura * (v_direcao.coords() / np.linalg.norm(v_direcao.coords()))
        self.__v_direcao = v_direcao.coords()
        self.__altura = altura
        self.__centro_base = centro_base.coords()
        self.__raio = raio
        self.cor = ""

    def intersection_with(self, reta):
        p_raio = self.__centro_base + self.__raio * np.array([1, 0, 0])
        geratriz = self.__vertice - p_raio
        cos_theta = self.__altura / np.linalg.norm(geratriz)
        v = self.__vertice - reta.p.coords()
        n = self.v_direcao / np.linalg.norm(self.v_direcao)
        a = np.power(produto_escalar(reta.v_direcao, n), 2) - \
            produto_escalar(reta.v_direcao, reta.v_direcao) * np.power(cos_theta, 2)
        b = 2 * (produto_escalar(v, reta.v_direcao) * np.power(cos_theta, 2) - produto_escalar(v, n) * produto_escalar(
            reta.v_direcao, n))
        c = np.power(produto_escalar(v, n), 2) - produto_escalar(v, v) * np.power(cos_theta, 2)
        tint = roots(a, b, c)

        # TODO corrigir comportamento da validação
        print(f" tint: {len(tint)}", end=" ")
        if len(tint) == 0:
            print("")
        index = 0
        for x in tint:
            print(f"tintA: {tint} x:{x} index: {index} ", end=" ")
            p = reta.ponto(x)
            k = self.vertice - p.coords()
            if (produto_escalar(k, n) >= 0) and (produto_escalar(k, n) <= self.altura):
                index = index + 1
                print("DONT REMOVE", end=" ")
            else:
                tint.pop(index)
                # tint.pop(index)
                print("REMOVE", end=" ")
            print(f"tintD: {tint}")
        return tint

    # Método getters
    @property
    def vertice(self):
        return self.__vertice

    @property
    def altura(self):
        return self.__altura

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

    @raio.setter
    def raio(self, r):
        self.__raio = r

    def set_cor(self, c):
        self.cor = c
