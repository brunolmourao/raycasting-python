""""
Classe do Objeto Esfera
A classe Esfera representa uma esfera onde:
p é	um ponto qualquer da superfície da esfera;
c é	o centro da esfera; e
r é	o raio da base do cone.
"""


class Sphere:
    # Método Construtor
    def __init__(self, p, c, r):
        self.__p = p
        self.__c = c
        self.__r = r

    # Método getters
    @property
    def p(self):
        return self.__p

    @property
    def c(self):
        return self.__c

    @property
    def r(self):
        return self.__r
