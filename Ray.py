"""""
Classe do Objeto Raio
A classe Raio representa uma reta que tem inicio em P0 e direção representada pelo vetor n que deve ser normalizado .
"""


class Ray:
    # Método Construtor
    def __init__(self, p0, vet_n):
        self.__p0 = p0
        self.__vet_n = vet_n
        self.t = 1

    def eq(self, t):
        return self.__p0 + t * self.__vet_n

    # Método getters
    @property
    def p0(self):
        return self.__p0

    @property
    def vet_n(self):
        return self.__vet_n
