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


class Sphere:
    # Método Construtor
    def __init__(self, centro, raio):
        self.__centro = centro
        self.__raio = raio

    @staticmethod
    def contem(self, ponto):
        eq = produto_escalar(ponto - self.__centro, ponto - self.__centro)
        if eq == (self.__raio * self.__raio):
            return True
        else:
            return False

    def intersection_with(self, reta):
        a = produto_escalar(reta.vet_n, reta.vet_n)
        b = produto_escalar(reta.__p - self.__centro, reta.__v_normal)
        c = produto_escalar(reta.__p - self.__centro, reta.__p - self.__centro) - self.__raio * self.__raio
        return roots(a, b, c)

    # Método getters
    @property
    def centro(self):
        return self.__centro

    @property
    def raio(self):
        return self.__raio
