import numpy as np


class Point:
    contador = 0
    def __init__(self, x, y, z):
        self.id = contador +1
        self.__x = x
        self.__y = y
        self.__z = z
        Point.contador = self.id

    def distancia(self, ponto):
        return np.sqrt(np.power(ponto.__x - self.__x, 2)
                       + np.power(ponto.__y - self.__y, 2)
                       + np.power(ponto.__z - self.__z, 2))

    def print_ponto(self):
        print(self.__x, self.__y, self.__z)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z
