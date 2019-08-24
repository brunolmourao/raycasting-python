""""
Classe do Objeto Cone
A classe Cone representa um cone onde:
p é	um ponto qualquer da superfície do cone;
v é	o vértice do cone;
n é	o vetor	unitário que define	a direção e	o sentido do eixo do cone;
theta é	o ângulo que a geratriz	forma com o	eixo do	cone;
h é	a altura do	cone; e
r é	o raio da base do cone.
"""


class Cone:
    # Método Construtor
    def __init__(self, p, v, n, theta, h, r):
        self.__p = p
        self.__v = v
        self.__n = n
        self.__theta = theta
        self.__h = h
        self.__r = r

    # Método getters
    @property
    def p(self):
        return self.__p

    @property
    def v(self):
        return self.__v

    @property
    def n(self):
        return self.__n

    @property
    def theta(self):
        return self.__theta

    @property
    def h(self):
        return self.__h

    @property
    def r(self):
        return self.__r
