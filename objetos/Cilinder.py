""""
Classe define um objeto Cilindro Reto.
Atributos:
    centro_base: Ponto
        Ponto com as coordenadas do centro da base
    raio: float
        Tamanho do raio da base do cilindro
    altura: float
        Altura do cilindro
    v_direcao: Vetor
        Vetor unitário que define a direção do eixo do cilindro
"""
import numpy as np

from auxiliar.CalcWithVectors import norma
from auxiliar.CalcWithVectors import produto_escalar
from auxiliar.QuadraticOperations import roots
from objetos.Ray import Ray


class Cillinder:
    # Método Construtor
    def __init__(self, centro_base, raio, altura, v_direcao):
        self.__centro_base = centro_base
        self.__raio = raio
        self.__altura = altura
        self.__v_direcao = v_direcao
        self.__cor = '_'

    def ponto(self, t):
        rq = produto_escalar(self.__raio, self.__raio)
        sub = Ray.ponto(t) - self.__centro_base
        prod_esc_sub = produto_escalar(sub, self.__v_direcao)
        vet_norm = sub - produto_escalar(prod_esc_sub, self.__v_direcao)
        result = produto_escalar(norma(vet_norm), norma(vet_norm))
        if result == rq and 0 <= prod_esc_sub <= self.__altura:
            return True
        else:
            return False

    def intersection_with(self, reta):
        t = []
        w = self.__calc_coefficients__(reta.v_direcao.to_array())
        v = self.__calc_coefficients__(reta.p.to_array() - self.__centro_base.to_array())
        a = produto_escalar(w, w)
        b = produto_escalar(v, w)
        c = produto_escalar(v, v) - produto_escalar(self.__raio, self.__raio)
        t = roots(a, b, c)
        return t

    def __calc_coefficients__(self, coe):
        return coe - produto_escalar(produto_escalar(coe, self.__v_direcao.to_array()), self.__v_direcao.to_array())

    # Método getters
    @property
    def centro_base(self):
        return self.__centro_base

    @property
    def raio(self):
        return self.__raio

    @property
    def altura(self):
        return self.__altura

    @property
    def v_direcao(self):
        return self.__v_direcao

    # Métodos setter
    @centro_base.setter
    def centro_base(self, v):
        self.centro_base = v

    @v_direcao.setter
    def v_direcao(self, v):
        self.__v_direcao = v

    @altura.setter
    def altura(self, a):
        self.__altura = a

    @raio.setter
    def raio(self, r):
        self.__raio = r

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor
