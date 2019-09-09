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
from utils.Ray import Ray
from utils.CalcWithVectors import produto_escalar
from utils.CalcWithVectors import norma
from utils.QuadraticOperations import roots


class Cillinder:
    __prop_obj_d = []
    __prop_obj_s = []

    # Método Construtor
    def __init__(self, centro_base, raio, altura, v_direcao):
        self.__centro_base = np.array(centro_base)
        self.__raio = raio
        self.__altura = altura
        self.__v_direcao = np.array(v_direcao)

    @staticmethod
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
        w = self.__calc_coefficients__(reta.v_normal)
        v = self.__calc_coefficients__(reta.p - self.__centro_base)
        a = produto_escalar(w, w)
        b = produto_escalar(v, w)
        c = produto_escalar(v, v) - self.__raio * self.__raio
        return roots(a, b, c)

    def __calc_coefficients__(self, coe):
        return coe - produto_escalar(produto_escalar(coe, self.__v_direcao), self.__v_direcao)

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
