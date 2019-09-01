""""
Classe do Objeto Esfera
A classe Esfera representa uma esfera onde:
    centro: Ponto
        centro é o centro da esfera;
    raio: float
        Raio da esfera.
"""
from auxiliar.CalcWithVectors import produto_escalar
from auxiliar.QuadraticOperations import roots
from objetos.Ray import Ray


class Sphere:
    # Método Construtor
    def __init__(self, centro, raio):
        self.__centro = centro
        self.__raio = raio

    @staticmethod
    def ponto(self, t):
        pt = Ray.ponto(t)
        result = produto_escalar(pt - self.__centro, pt - self.__centro)
        rq = produto_escalar(self.__raio, self.__raio)
        if result == rq:
            return True
        else:
            return False

    def intersection_with(self, reta):
        rq = produto_escalar(self.__raio, self.__raio)
        a = produto_escalar(reta.v_normal, reta.v_normal)
        b = produto_escalar(reta.p - self.__centro, reta.v_normal)
        c = produto_escalar(reta.p - self.__centro, reta.p - self.__centro) - rq
        return roots(a, b, c)

    # Método getters
    @property
    def centro(self):
        return self.__centro

    @property
    def raio(self):
        return self.__raio
