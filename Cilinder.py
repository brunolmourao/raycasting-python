""""
Classe do Objeto Cilindro
A classe Cillinder representa um cilindro onde:
p é um ponto qualquer da superfície	do cilindro;
b é	centro da base do cilindro;
u é	o vetor	unitário que define	a direção e	o sentido do eixo do cilindro;
h é	a altura do	cilindro; e
r é	o raio do cilindro.
"""


class Cillinder:
    # Método Construtor
    def __init__(self, p, b, u, h, r):
        self.__p = p
        self.__b = b
        self.__u = u
        self.__h = h
        self.__r = r

    # Método getters
    @property
    def p(self):
        return self.__p

    @property
    def b(self):
        return self.__b

    @property
    def u(self):
        return self.__u

    @property
    def h(self):
        return self.__h

    @property
    def r(self):
        return self.__r
