""""
Classe do Objeto Esfera
A classe Esfera representa uma esfera onde:
    centro: Ponto
        centro é o centro da esfera;
    raio: float
        Raio da esfera.
"""


class Sphere:
    # Método Construtor
    def __init__(self, centro, raio):
        self.__centro = centro
        self.__raio = raio

    # Método getters
    @property
    def centro(self):
        return self.__centro

    @property
    def raio(self):
        return self.__raio
